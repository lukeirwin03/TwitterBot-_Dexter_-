import tweepy
import configparser
from time import sleep
import textGenerationHappyTransformer as textGen

config = configparser.ConfigParser()
config.read('config.ini')
FILE = 'id.txt'

# getting the information from the config.ini file
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
user_ID = config['twitter']['user_ID']

def authenticate():
    '''Authenticates the informations and creates the api object

    :rtype: object
    :return: tweepy api object
    '''
    auth = tweepy.OAuthHandler(api_key,api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def retrieve_id(file):
    '''Gets the tweet id of the last tweet that has been replied to

    :param file: the name of the file has the last seen tweet's ID written to it
    :type file: string
    :rtype: int
    :return: the tweet id of the last tweet that has been replied to
    '''
    reader = open(file, 'r')
    last_seen_id = int(reader.read().strip())
    reader.close()
    return last_seen_id

def store_id(id, file):
    '''Stores the id of the last seen tweet to the file

    :param id: the id of the tweet that the bot is replying to
    :type id: int
    :param file: the name of the file has the last seen tweet's ID written to it
    :type file: string 
    '''
    writer = open(file, 'w')
    writer.write(str(id))
    writer.close()

def reply(api):
    '''Uses the api object to reply to any tweets if there are any.

    :param api: tweepy api object
    :type api: object
    '''
    last_seen_id = retrieve_id(FILE)
    mentions = api.mentions_timeline(since_id=last_seen_id)

    for mention in reversed(mentions):
        if 'HeyDexter' in mention.text:
            message = (mention.text.split('HeyDexter', 1)[1])
            last_seen_id = mention.id
            store_id(last_seen_id, FILE)
            tweet_to_quote_url = f'http://twitter.com/{mention.user.screen_name}/status/{mention.id}'
            api.update_status(status=('@' + mention.user.screen_name + ' ' + textGen.dialoGPT(message)), auto_populate_reply_metadata=True, attachment_url=tweet_to_quote_url)
            print('Replied to @'+mention.user.screen_name)

def main():
    api = authenticate()
    while True:
        reply(api)
        sleep(10)

if __name__ == '__main__':
    main()