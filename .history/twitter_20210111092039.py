import tweepy
import smtplib
auth = tweepy.OAuthHandler('ekaUywgWfrMWeaNx7AVrG4KYZ', 'yaQQtPTrw7sgwtisn5XDR8Aj8Sbe4CK9X36uXaBBWPbLB1ndjY')
auth.set_access_token('1140784506909208576-PKNBHBfB3DHCc49ubLngzRGP56TG2O', 'QccH2KyqKjPx0DpcWx9GmzR79WZcqJyxQasQX95DFbaSs')

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     if(tweet.user.name == 'NBA'):
#         api.update_status(status = 'Lebron is goat', in_reply_to_status_id = tweet.id, auto_populate_reply_metadata = True)
arr_of_tweets = []

class TwitterStreamListener(tweepy.StreamListener):
    def on_error(self, status_message):
        if(status_message == 420):
            return False
    def on_status(self, status):
        print(status.text)
        arr_of_tweets.append(status)
        if(len(arr_of_tweets) == 5):
            return False
    
def send_mail(tweets):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('imran.siraj6450@gmail.com', 'vzjuzvlcphxxiexp')

    subject = 'News Tweets'
    body = f"""{tweets[0].user.name}: {tweets[0].text} (https://twitter.com/i/web/status/{tweets[0].id_str})\n{tweets[1].user.name}: {tweets[1].text} 
    (https://twitter.com/i/web/status/{tweets[1].id_str})\n{tweets[2].user.name}: {tweets[2].text} (https://twitter.com/i/web/status/{tweets[2].id_str})\n{(tweets[3].user.name)}: {tweets[3].text} 
    (https://twitter.com/i/web/status/{tweets[3].id_str})\n{tweets[4].user.name}: {tweets[4].text} (https://twitter.com/i/web/status/{tweets[4].id_str})"""

    message = 'Subject: {}\n\n{}'.format(subject, body)
    server.sendmail('imran.siraj6450@gmail.com', 'isiraj7289@bths.edu', message.encode('ascii', 'ignore'))
    print('Email has been sent!')
    server.quit()

streamListener = TwitterStreamListener()
stream = tweepy.Stream(auth = api.auth, listener = streamListener)

stream.filter(follow = ['428333', '807095', '2467791'], track = ['President Trump'], languages = ['en'])
send_mail(arr_of_tweets)



