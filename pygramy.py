#!/usr/bin/env python3
#
# pygramy.py - Make an OSINT scraper on instagram without login
#
##########################################################################
# Get information from an user account where login is no needed.         #
##########################################################################
#
#
# Historic:
#
# v0.1-BETA 29-12-2022
#	- Created the program
#	- Comentary improvement
#	- Launched the BETA
#
##########################################################################									 #
#									 #
#           It can be cruel, poetic or blind. But when its		 #
# 		  denied is the violence you may find.			 #
#									 #
##########################################################################

#############
# Libraries #
#############

import argparse
from instagramy import *
from os import system as exe



exe("clear")

argumento = argparse.ArgumentParser(usage="python3 pygram.py -a [USER] [PATTERNS]", description="User insta scraper")

##################
#    Arguments   #
##################


argumento.add_argument("-u", "--user-account", type=str, help="Set the user to scrap", required=True)
argumento.add_argument("--followers", help="Check the number of followers", action="store_true")
argumento.add_argument("--biography", help="See biography user", action="store_true")
argumento.add_argument("--followings", help="See the number of followings", action="store_true")
argumento.add_argument("--fullname", help="Show fullname of the user", action="store_true")
argumento.add_argument("-priv", help="Check if the account is private", action="store_true")
argumento.add_argument("-site", help="Get the website or url of the user", action="store_true")
argumento.add_argument("-pp", "--profile-picture", help="Get the profile picture of the user", action="store_true")
argumento.add_argument("-usernamem", help="Display username", action="store_true")
argumento.add_argument("-posts", help="Show the posts", action="store_true")
argumento.add_argument("-pdu", "--posts-display-urls", action="store_true")
argumento.add_argument("-json", help="Get the Json", action="store_true")
argumento.add_argument("-jr", "--joined-recently", help="Check if the account is joined recently", action="store_true")
argumento.add_argument("-np", "--number-of-posts", help="Display the number of posts", action="store_true")
argumento.add_argument("--country-block", help="Check if has country block", action="store_true")
argumento.add_argument("-oinfo", "--other-info", help="", action="store_true")


args = argumento.parse_args()



#######################################################
#print(args) # Just enable to check arguments output  #
#######################################################


##########################################
#           DEFAULT VARIABLES            #
##########################################


username = args.user_account
session_id = "38566737751%3Ah7JpgePGAoLxJe%334" # Put your session id instagram
followers = args.followers
biography = args.biography
followings = args.followings
fullname = args.fullname
private = args.priv
site = args.site
profile_picture = args.profile_picture
username_atrribute = args.usernamem
posts = args.posts
posts_urls = args.posts_display_urls
json = args.json
joined_recently = args.joined_recently
number_of_posts = args.number_of_posts
country_block = args.country_block
other_info = args.other_info


#################################################
# 	     Setinng up functions		#
#################################################

def followers_check():

	user = InstagramUser(username, sessionid=session_id)
	return (f"Followers: {user.number_of_followers}")


def call_biography():

	user = InstagramUser(username, sessionid=session_id)
	return (f"Biography: {user.biography}")


def followings_check():

	user = InstagramUser(username, sessionid=session_id)
	return (f"Followings: {user.number_of_followings}")


def show_fullname():

	user = InstagramUser(username, sessionid=session_id)
	return (f"Fullname: {user.fullname}")


def check_private_account():

	user = InstagramUser(username, sessionid=session_id)
	return (f"PRIVATE ACCOUNT: {user.is_private}")


def url_from_user():

	user = InstagramUser(username, sessionid=session_id)
	return (f"SITE: {user.website}")


def get_profile_picture():

	user = InstagramUser(username, sessionid=session_id)
	return (f"LINK OF THE PROFILE PICTURE: {user.profile_picture_url}")


def username_atributte():

	user = InstagramUser(username, sessionid=session_id)
	return (f"USERNAME: {user.username}")


def get_posts():

	user = InstagramUser(username, sessionid=session_id)
	return (f"POSTS: {user.posts}")


def posts_urls():

	user = InstagramUser(username, sessionid=session_id)
	return (f"POSTS URLS: {user.posts_display_urls}")


def json():

	user = InstagramUser(username, sessionid=session_id)
	return (f"JSON: {user.get_json}")


def joined_recently():

	user = InstagramUser(username, sessionid=session_id)
	return (f"JOINED RECENTLY: {user.is_joined_recently}")



def number_of_posts():

	user = InstagramUser(username, sessionid=session_id)
	return (f"NUMBER OF POSTS: {user.number_of_posts}")

def country_block():

	user = InstagramUser(username, sessionid=session_id)
	return (f"BLOCKED ON COUNTRY: {user.has_country_block}")


def other_info():

	user = InstagramUser(username, sessionid=session_id)
	return (f"Others informations: {user.other_info}")

# Call functions

if followers == True:

	print(followers_check())

if biography == True:

	print(call_biography())

if followings == True:

	print(followings_check())

if fullname == True:

	print(show_fullname())

if private == True:

	print(check_private_account())

if site == True:

	print(url_from_user())

if profile_picture == True:

	print(get_profile_picture())

if username_atrribute == True:

	print(username_atributte())

if posts == True:

	print(get_posts())

if posts_urls == True:

	print(posts_urls())

if json == True:

	print(json())

if joined_recently == True:

	print(number_of_posts())

if number_of_posts == True:

	print(number_of_posts())

if country_block == True:

	print(country_block())

if other_info == True:

	print(other_info())

