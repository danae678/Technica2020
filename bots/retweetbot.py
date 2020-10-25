#code for the bot
import tweepy, time, sys, os
from dotenv import load_dotenv

load_dotenv()

#these are where the API Tokens that Morgan set up will go, when the applicaton is approved
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_KEY = os.getenv('ACCESS_KEY')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

#set up twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#query will hold the phrase(s) we want to search for
#tweets per query sets a limit for how many we search for, we can change this later
query = "#RosesBot"
tweets_per_query = 10


print ("searching for: " + query) 

def retweet_hashtag():
	new_tweets = 0 #counts the number of tweets
	#this will get the results of our search and loop through them. It will also filter out retweets using "-filter:retweets" so we only see original tweets
	for tweet in tweepy.Cursor(api.search, q = query +" -filter:retweets", tweet_mode = "extended").items(tweets_per_query):
		user_name = tweet.user.screen_name #gives us the users name who tweeted
		id = tweet.id #gets the id of the tweet
		url = 'https://twitter.com/' + user_name +'/status/' +str(id) #creates the URL of the tweet
		

		#this will retweet the tweet found, unless it's already been retweeted
		if not (tweet.retweeted):
			try:
				tweet.retweet()
				print("Retweeting tweet by @" + user_name)
				print(url)
				print("\t ***successfully retweeted***")
				new_tweets += 1
				time.sleep(60)

			except tweepy.TweepError as e:
				pass

			except StopIteration:
				break
	print("\nTotal new tweets: " + str(new_tweets))

while True:
	retweet_hashtag()
	time.sleep(300) #searches every 5 minutes

