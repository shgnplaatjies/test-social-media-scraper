from threading import TIMEOUT_MAX
import tweepy
import config
import signal

def authenticateConfig():
    # Authenticate to Twitter    
    try: 
        auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET_KEY)
        auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth) # Setting these properties true will make the api to automatically wait for rate limits to replenish

        print("Authentication successful") # Prints the name of the authenticated user

        return api # Return the api object to caller
    except tweepy.HTTPException as e:
        print( "Error: Authentication Failed -", str(e))
        return None # Return None to caller (TODO: add error handling)
    
    
    
if __name__ == "__main__":
    authenticateConfig()