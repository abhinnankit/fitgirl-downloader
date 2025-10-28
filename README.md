# Fitgirl-downloader

Downloads FuckingFast links from fitgirl-repacks.site links page

## Requirements

This is a Python script and some basic knowledge of Python3 is required.

Also, make sure to have Python installed in your system. Download Chromedriver for your respective systems. (Follow any guide on Youtube to install Python, if you don't already have it)

## Steps

Download the repo or just the file, downloader[,2].py

Open Terminal for Mac/Windows or Powershell for Windows

### Create new venv

Mac - python3 -m venv .venv

Windows - python -m venv .venv

### Activate venv

Mac - source venv/bin/activate

Windows - .\\venv\Scripts\Activate.ps1

If you are unable to run the above command in Powershell/Terminal on Windows because of execution policy error. Refer: <https://learn.microsoft.com/en-gb/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4>

### Install the dependencies using

pip install -r requirements.txt

### Update some links

Update

WEBSITE_URL with the one you need

DOWNLOAD_DIR with your default Chrome download directory

Eg.

For Mac - see DOWNLOAD_DIR value in downloader.py

For Windows - see DOWNLOAD_DIR value in downloader2.py

### Execute the following to start the Downloads

Mac - python3 downloader.py

Windows - python downloader2.py

For eg:

python downloader.py

### Deactivate venv using

deactivate
