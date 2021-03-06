[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/arcelioeperez/dash-app) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Pandas)](https://pandas.pydata.org/) ![Lines of code](https://img.shields.io/tokei/lines/github/arcelioeperez/dash-app)  

# This is a Dash App for my internship at The GreatFull Plate  
Author: Arcelio E. Perez  

URL for the Heroku app: [click here](https://my-internship-app.herokuapp.com/)  
URL for the Github website (contains the links, pdf, and files needed for this project): [click here](https://arcelioeperez.github.io/dash-app/)  

**Supported OS: Ubuntu, Windows, MacOS**  
Also included: Dockerfile  

Basic requirements: python 3, requirements.txt, and app.py   
Files for Docker: docker_app.py and Dockerfile  - this assumes that you have Docker installed in your computer. If not, refer to [DockerNotes](https://arcelioeperez.github.io/dash-app/DockerNotes) and [Docker.com](https://www.docker.com/).  

**To know more about this project, please read the [Wiki Page](https://github.com/arcelioeperez/dash-app/wiki).**  

### App Demo 
![Demo GIF](demo/my-dash-app.gif)  

### Cloning the repository  
```
git clone https://github.com/arcelioeperez/dash-app.git && cd dash-app
```  
If you download a `.zip` folder or `tar.gz`  
```
unzip nameofthezipped folder
#for tar.gz
tar -xvf nameofthetar folder
```  
### Running the app - once the website folder has been downloaded and unzipped  
``` 
# Go to the folder typing 
cd foldername 
```  
### To run the file that contains the dash app, in this case **app.py**    

>*On Windows make sure you have Python in the **path** otherwise it won't work* --  
>Here's a [link](https://docs.python.org/3/using/windows.html) that explains the process of adding Python to the path.  

``` 
python3 app.py
```  
This will render the localhost address, this address can then be opened in the browser of choice.  

**Note:** if you do not have the required packages you must type this in your command prompt or terminal:     
``` 
#MacOS or Linux
pip3 install -r requirements.txt
#Windows 
pip install -r requirements.txt
```  
*requirements.txt* contains all the libraries and dependencies needed to run **app.py**  
View the requirements.txt file here: [view](https://raw.githubusercontent.com/arcelioeperez/dash-app/main/assets/requirements.txt)  
Download the requirements.txt file here: <a href="/requirements.txt" download>requirements.txt</a>  

If you want to fork or clone the directory feel free to do so. From the [Github URL](https://arcelioeperez.github.io/dash-app/) there are two download buttons for `.zip` and `.tar.gz` files  

Running the `eapp` executable  
Creating the executable  
```
chmod +x eapp
```  
The first line of this script is the location of the Python3 interpreter. If you are running Windows you might have a different interpreter. These are [common problems that could happen when running the scripts and their solutions](https://arcelioeperez.github.io/dash-app/Troubleshooting).  
```
#!/usr/bin/env python3
```
To run  
```
./eapp 
```

Running from VIM  
On `visual` mode type: 
```
:!python3 %
```  
If you want to map commands you must go to the `.vimrc` file and type:  
```
command P:!python3 %
```
Now to run you just have to type: 
```
:P
```  

Running from GNU-Emacs  
```
#open a shell window
M-x shell
#or - if using a makefile
M-x compile
```  
After opening the shell window you just have to type `python3 nameofthefile.py`  

Text editors used: VS Code, GNU-Emacs, and VIM.  
Download GNU-Emacs - MacOS:
```
brew cask install emacs
```  
*VIM should be already installed. To open VIM, go to the terminal and type: `vim`.*  

Download GNU-Emacs - GNU-Linux Ubuntu:  
```
sudo add-apt-repository ppa:kelleyk/emacs
sudo apt update
sudo apt install emacs27
```  

If you would like to configure VIM, go to the `.vimrc` file and make the changes you want.  

If you would like to configure GNU-Emacs, go to the `.emacs`, `.init.el`, or `emacs.el` file and make the changes you want. 

Python version: Python 3.7.3 (mostly run with Windows 10, WSL Debian). Other operating systems used: MacOS and Ubuntu (20.04.1 LTS).  
Check Python version with:  
```
python3 -V
```  

**If there is a bug or mistake, please report it so that I can correct it. Thank you!**  

**Works Cited:** [Here](Citation.md)
