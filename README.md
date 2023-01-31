# Science_Stegano

Science_Stegano is a python project in which we hide the secret message inside any image using Tkinter and the PIL module.

## What is Image Steganography?

 steganography technique involves hiding sensitive information within an ordinary, non-secret file or message, so that it will not be detected. The sensitive information will then be extracted from the ordinary file or message at its destination, thus avoiding detection. Steganography is an additional step that can be used in conjunction with encryption in order to conceal or protect data.


Steganography is a means of concealing secret information within (or even on top of) an otherwise mundane, non-secret document or other media to avoid detection. It comes from the Greek words steganos, which means “covered” or “hidden,” and graph, which means “to write.” Hence, “hidden writing.”

You can use steganography to hide text, video, images, or even audio data. It’s a helpful bit of knowledge, limited only by the type of medium and the author’s imagination.


### project preq

This project requires good knowledge of python and the Tkinter library. 
tkinter is module that is frequently used to build graphical interface in many language GUI.

and we will need also Pillow.
This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

```
python -m pip install pillow
```

## Requirements

```
cffi==1.15.1
cryptography==39.0.0
Pillow==9.4.0
pycparser==2.21
```

## and for you benefice, use a virtual environement :

### creating a venv for windows\Linux\Mac :

```
python -m venv <directory>
```
### activating venv 

for Windows :

```
# cmd
venv\scripts\activate.bat
# powershell 
venv\scripts\Activate.ps1
```

for Linux\Mac :

```
source myvenv/bin/activate
```

### what's inside a venv?

for windows :

```
.
├── Include
├── Lib
│   └── site-packages
├── pyvenv.cfg
└── Scripts
    ├── activate
    ├── activate.bat
    ├── Activate.ps1
    ├── deactivate.bat
    ├── pip3.10.exe
    ├── pip3.exe
    ├── pip.exe
    ├── python.exe
    └── python.exe
````
for Linux\Mac:
```
.
|--bin
|   |--activate
|   |--activate.csh
|   |--activate.fish
|   |--easy_install
|   |--easy_install-3.7
|   |--pip
|   |--pip3
|   |--pip3.7
|   |--python->python3
|   |--python3->/usr/local/bin/python3
|
|--include
|--lib
|   |--python3.7
|         |--site-packages
|--pyvenv.cfg
```

### deactivating a venv

Once you have finished working on your project, it’s a good habit to deactivate its venv. By deactivating, you leave the virtual environment. Without deactivating your venv, all other Python code you execute, even if it is outside your project directory, will also run inside the venv.

```
deactivate
```


uninstall all package 
````
pip freeze | xargs pip uninstall -y
````

## the package that i created is joyboy 0.0.1 

to run the project , you need to install all the pre-requis of the project , I just mention it on the requirements file . so you need to install them all .
then run to python interpreter or a python file and tap this code :
```
from mypackage import main
```
then run the file.

```
ENJOY IT 👍🙂
```


