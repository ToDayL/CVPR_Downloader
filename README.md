# CVPR Downloader

CVPR Papers download scripts for CVPR 2017 and CVPR 2018.

## Requirement

python3, bs4, requests.

Use pip to install bs4 and requests.

```Shell
sudo pip3 install bs4
sudo pip3 install requests
```

Tested in Ubuntu 16.04, python3.5 

## Usage

For CVPR 2018:

```Shell
cd CVPR_2018
mkdir Papers
cd Scripts
pyhton3 ./HTML_Parser.py
```

## Others

Script for CVPR 2017 will automatically read HTML file from the CVPR main conference page and get the Session title. Papers are categorised according to their topic.

CVPR 2018 does not offer session title for every page, so the papers are not categorised. But script for CVPR 2018 should work with any conference in cv-foundation open access. http://openaccess.thecvf.com/menu.py


