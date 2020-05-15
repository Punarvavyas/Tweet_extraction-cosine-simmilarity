
import tweepy, time, csv

consumer_key = "nbQQrucJZi1JSPT8G3zVFR77z" # insert your consumer_key
consumer_secret = "f7xFboiaPa8Ljcg7OaKJPFDu0CsPFUjjH7sKPaJAPVQzf1KLpP"
#er_secret
access_key = "846238461258551296-QRpSpwQKiFCdjEOqBTUzQWMNqm3MIFc" # i
access_secret = "IgZ99GyksfNsxJEsepUIOSVa01YE62nNKj5jMLP5UF6So" #


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# this function collects a twitter profile request and returns a Twitter object
def get_profile(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        # https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-show
        # describes get_user
        user_profile = api.get_user(screen_name)
    except Exception as e:
        return "There was an error. Details:" + e
    return user_profile

#this function collects twitter profile tweets and returns Tweet objects
def get_tweets(screen_name):
    try:
        # https://developer.twitter.com/en/docs/tweets/timelines/overview describes user_timeline
        tweets = api.user_timeline(screen_name, count=20)
    except Exception as e:
        return "There was an error. Details:" + e
    return tweets

# set of profiles that we want to obtain.
profiles = ["google", "msdev","rosiebarton","realDonaldTrump"]

with open ('tweets.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id","screen_name","created_at","text"])
    for profile in profiles:
        t = get_tweets(profile)
        for tweet in t:
            writer.writerow([str(tweet.id),tweet.user.screen_name,tweet.created_at,tweet.text])
            # or
            # tweet = tweet._json
            # writer.writerow([tweet["id"],tweet["user"]["screen_name"],tweet["created_at"],tweet["text"].encode("utf-8")])