from playsound import playsound
import tweepy
import smtplib
import email_sound.aifc


auth = tweepy.OAuthHandler('ekaUywgWfrMWeaNx7AVrG4KYZ', 'yaQQtPTrw7sgwtisn5XDR8Aj8Sbe4CK9X36uXaBBWPbLB1ndjY') # Authenticate API keys
auth.set_access_token('1140784506909208576-PKNBHBfB3DHCc49ubLngzRGP56TG2O', 'QccH2KyqKjPx0DpcWx9GmzR79WZcqJyxQasQX95DFbaSs') # Authenticate API token access. 

api = tweepy.API(auth) # api object to use api methods.

arr_of_tweets = [] # ADT to store tweets.

# The TwitterStreamListener class creates an object instance that records the tweets streamed and allows for the user to use methods to access and use the data.
num_of_tweets = input('How many tweets would you like?: \n')
class TwitterStreamListener(tweepy.StreamListener):
    def on_error(self, status_message):
        if(status_message == 420):
            return False

    # on_status appends every tweet the object records and appends the tweet to an array.
    # @self refers to the object instance.
    # @status refers to the current tweet the listener is on.
    # Returns false once 10 tweets are streamed.
    def on_status(self, status):
        print(status.text)
        arr_of_tweets.append(status)
        if(len(arr_of_tweets) == int(num_of_tweets)):
            return False

# send_mail sends 5 of the tweets streamed from the arr_of_tweets array to my email.
# @tweets will contain the array of the tweets streamed.
def send_mail(tweets):
    server = smtplib.SMTP('smtp.gmail.com', 587) # Creates an SMTP Server.
    server.starttls() # Starts the server.
    server.login('imran.siraj6450@gmail.com', 'vzjuzvlcphxxiexp') # The login credentials for who is senidng the email.

    subject = 'News Tweets'

    # body is a variable that is a formatted version for the tweets that are sent to the email.
    # Each tweet will occupy a row that has the username of the person who sent the tweet, the text of the tweet, and the link of the tweet.
    body = f"""{(tweets[0].user.name)}: {(tweets[0].text)} (https://twitter.com/i/web/status/{tweets[0].id_str})\n{(tweets[1].user.name)}: {(tweets[1].text)} 
    (https://twitter.com/i/web/status/{tweets[1].id_str})\n{(tweets[2].user.name)}: {(tweets[2].text)} (https://twitter.com/i/web/status/{tweets[2].id_str})\n{(tweets[3].user.name)}: 
    {(tweets[3].text)} (https://twitter.com/i/web/status/{tweets[3].id_str})\n{(tweets[4].user.name)}: {(tweets[4].text)} (https://twitter.com/i/web/status/{tweets[4].id_str})"""

    message = 'Subject: {}\n\n{}'.format(subject, body) # Message sent for the email.
    server.sendmail('imran.siraj6450@gmail.com', input('Enter your email to get the news tweets!: \n'), message.encode('ascii', 'ignore')) # The email with the tweets will be sent from my personal email to my school email.
    playsound(email_sound)
    print('Email has been sent!')
    server.quit() # The SMTP server stops once the email has been sent.

streamListener = TwitterStreamListener() # Instance of TwitterStreamListener.
stream = tweepy.Stream(auth = api.auth, listener = streamListener) # Stream of tweets which the streamListener object will record.

stream.filter(follow = ['428333', '807095', '2467791'], track = ['President Trump', 'News'], languages = ['en']) # This will filter the stream of tweets. I will only get tweet that contain the words 'President Trump' as he popular on the news currently.
send_mail(arr_of_tweets) # Sends the array of tweets to my email.



