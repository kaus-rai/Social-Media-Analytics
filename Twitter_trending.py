import tweepy
import constant as con

auth = tweepy.OAuthHandler(con.consumer_key,con.consumer_secret)
auth.set_access_token(con.access_token,con.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)