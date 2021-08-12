# STAR_Lab pedestrian detection model development 
---
This document will go through the steps to perform pedestrian detection on your machine

## software and environment setup

1. Install [anaconda](https://www.anaconda.com/products/individual#Downloads "anaconda download link") and [jupyter notebook](https://jupyter.org/install "jupyter notebook download link").
1. Clone this [repository](https://github.com/prism5426/STARLAB "repo link") repository.
1. After repository is cloned, go to the directory using **cmd prompt** in Windows and **Terminal** in Linux or MacOS.
1. Create a new conda virtual enviroment (Using python enviroment might cause access issue, but should also work)

    ```conda create -n myenv python=3.8```
1. Activate environment

    ```conda activete myenv```
1. Upgrade pip

    ```python -m pip install -upgrade pip```
1. Add virtual environment to kernel

    ```pip install ipykernel```

    ```python -m ipykernel install --user --name=myenv```
1. In the virtual environment and the repository directory, open up **jupyter notebook** and make sure the virtual environment is added to kernel