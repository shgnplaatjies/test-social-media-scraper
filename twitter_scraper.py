import pandas as pd
import tweepy
import config 
import auth
# Authenticate to Twitter
# This authentication approach isn't sustainable, temporarily solution for testing. 
# Transfer to OAuth2 and configparser for production.

        
def main():
    auth.authenticateConfig()
        

# If this script file's name is main, run the main function.
if __name__ == "__main__": 
    main()