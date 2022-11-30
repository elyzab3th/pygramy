<img src="/src/img/pygramy.png">
A basic tool for OSINT purposes made using python language where is for Instagram Scrapy without login required.



# Installation

```bash
clear && git clone https://github.com/Leandro-Leone/pygramy && cd pygram && python3 -m pip install -r requirements.txt

```


# Usage

```
usage: python3 pygram.py -a [USER] [PATTERNS]

User insta scraper

options:
  -h, --help            show this help message and exit
  -u USER_ACCOUNT, --user-account USER_ACCOUNT
                        Set the user to scrap
  --followers           Check the number of followers
  --biography           See biography user
  --followings          See the number of followings
  --fullname            Show fullname of the user
  -priv                 Check if the account is private
  -site                 Get the website or url of the user
  -pp, --profile-picture
                        Get the profile picture of the user
  -usernamem            Display username
  -posts                Show the posts
  -pdu, --posts-display-urls
  -json                 Get the Json
  -jr, --joined-recently
                        Check if the account is joined recently
  -np, --number-of-posts
                        Display the number of posts
  --country-block       Check if has country block
  -oinfo, --other-info

```

# 

<a href="https://asciinema.org/a/VeWodQLcmMWj9N9hvfrXtdoUE" target="_blank"><img src="https://asciinema.org/a/VeWodQLcmMWj9N9hvfrXtdoUE.svg" /></a>

# Generating a Binary - Useful for Windows O.S <img src="/src/img/binary-logo.svg" width="500" height="600" >

To use a binary file of the program actually there are 2 ways for it;

- Using from the repository

There is a binary on the repository and would be good a check on file.

- Generating yout own binary executable

If you'd like to generate your own binary then follow the next steps on your terminal:

## Sintax
```bash

pyinstaller --onefile [Name of the program to encode to a binary]
```

## Use the command bellow for generate your own binary:

```bash
pip installpyinstaller && pyinstaller --onefile pygramy.py
```
