import cv2 as cv

isObjectDetected = [0]
cumulative_counting = {'total': 0}

# cumulative object counting mode along y-axis
def horizontal_cumulative_counting(frame, detected_objects, roi_x=.5, direction='both', deviation=0.01):

    # added the x_centers(x, y) of all detected boxes to a list
    x_centers = []
    for i in range(len(detected_objects)):
        # bounding box is in the format of [y_up, x_left, y_down, x_right]
        coordinate = detected_objects[i]['box']
        x_centers.append((coordinate[3] - coordinate[1]) / 2)
        
    # detect if x_center of object crosses ROI
    insideROI = False # any object is inside ROI
    if direction == 'both':
        for i, x_center in enumerate(x_centers):
            if roi_x - deviation < x_center < roi_x + deviation:
                # object detected
                insideROI = True

                # update for all objects
                cumulative_counting.update({'total': cumulative_counting.get('total') + 1})

                # update for each object
                class_name = detected_objects[i]['class_name']
                if class_name not in cumulative_counting.keys():
                    cumulative_counting.update({class_name: 1})
                else:
                    cumulative_counting.update({class_name: cumulative_counting.get(class_name) + 1})

    elif direction == 'left_2_right':
        pass
    elif direction == 'right_2_left':
        pass

    # draw ROI line, red for regular, green if object is detected
    x1 = int(frame.shape[1] * roi_x)
    x2 = x1
    y1 = 0
    y2 = frame.shape[0]
    print(insideROI)
    if insideROI is False:
        cv.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
    else:
        cv.line(frame, (x1, y2), (x2, y2), (0, 255, 0), 2)

    return frame
    

