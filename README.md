# RPF
Official Code Repository for the paper Incorporating Relative Object Positioning for Image Captioning

This Repository will contain code for creating Relative Positioned Features for images and creation and evaluation of the AoANet+VC+RPF model.

All instructions assume you are running from RPF directory.

## Installation

### Install conda (optional)
We recommend installing conda to setup a sparate environment as this involves specific versions of certain libraries.

### Create Environment

For Linux and Mac
Open a terminal window in RPF directory.

````bash
sh install.sh "rpf"
````
This will create an environment called rpf(can be changed by replacing rpf with desired name) for this project and will install the required libraries for the project.

For Windows
Open a command prompt window in RPF directory.

````bash
conda create --name rpf
conda activate rpf
````
This will create an environment called rpf(can be changed by replacing rpf with desired name) for this project.

````bash
python3 install.py
````
