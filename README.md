# dex_the_bot on Twitter
------------------------------------------------------------------------------

## Description 
This is a Twitter bot that I build to experiment with the Tweepy API in hopes of doing more complicated projects with the API in the future. The bot's main function at the moment is to come up with a reply to a tweet when you tweet at it using the GPT Dialo model. dex_the_bot is designed to perform a different task depending on the hashtag that you include when tweeting at it. As of the current version, the only hashtag that there is is '#HeyDexter', which will just have the bot return a message after reading what was tweeted at it. The name is inspired from Dexter's Laboratory.

## Files in this Directory
- main.py
- textGenerationHappyTransformer.py
- LICENSE: Boost Software License 1.0
- This README

## Dependencies and Configuration Instructions
This program was written and tested in Python 3.9.10. Any IDE should work for this as long as you have all of the necessary modules and packages installed, such as the GPT Dialo model. You will also have to have a developer account set up with Twitter and have a config.ini file set up with all of your information to get the API working. The config.ini file should have the API Key, API Key Secret, Access Token, Access Token Secret, and User ID. 

## Install Instructions
You will need to satisfy all of the dependencies and then it should be ready to run, just be sure to change the hashtag that the bot will be looking to respond to, or don't, you will just need to account for that.

## Contact Info
Author: Luke Irwin, lukemirwin [at] gmail [dot] com  

## Known Bugs
As of 07/19/22 there are no known bugs in the program.
