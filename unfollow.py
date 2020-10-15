import tweepy
from keys import keys


SCREEN_NAME = keys['screen_name']
# # API key
CONSUMER_KEY = keys['consumer_key']
# # API key secret
CONSUMER_SECRET = keys['consumer_secret']
# # access_token
ACCESS_TOKEN = keys['access_token']
# # access_token_secret
ACCESS_TOKEN_SECRET = keys['access_token_secret']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

followers = api.followers_ids(SCREEN_NAME)
friends = api.friends_ids(SCREEN_NAME)

# Uncomment the lines below if you want to get a list of followers

# for f in friends[:10]:
#     print("ID: {} - Screen Name: {}".format(f, api.get_user(f).screen_name))

    
# Diplay a total number of followers
print(len(friends))

# Check the people I follow (friends)
# See if they are also in my followers list
# If you find any that are not following me ask if I want to unfollow
# using "api.destroy_friendship".
#
# friends[:100] = start from the beginning to the first 100 friends
# This helps me avoid hitting the twitter api rate limit
# for f in friends[:100]:
#     if f not in followers:
#         print("Unfollow {0}?".format(api.get_user(f).screen_name))
#         if input("Y/N?") == 'y' or 'Y':
#             api.destroy_friendship(f)

# We are doing the opposite of what this bot was created for.
# below, we are searching for followers we do not yet follow back to determine
# if we want to follow them.
for f in followers[:100]:
    if f not in friends:
        print("follow {0}?".format(api.get_user(f).screen_name))
        if input("Y/N") == 'y' or 'Y':
            api.create_friendship(f)