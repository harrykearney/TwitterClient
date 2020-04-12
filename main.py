import tweepy
import tkinter
from credentials import *

root = tkinter.Tk()
root.title('Custom Twitter Client')
root.geometry('960x540')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

title = tkinter.Label(root, text='Custom Twitter Feed', font=('Arimo', 22))
title.pack()

scrollbar = tkinter.Scrollbar(root)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

tweets = api.home_timeline()

# for tweet in tweets:
#     tweettext = tweet.text.encode('ascii', 'ignore').decode('ascii')
# 
#     tweetlabel = tkinter.Label(root, text=f'{tweet.author.name}: {tweettext}')
#     tweetlabel.pack()
# 
#     seperator = tkinter.Label(root, text='-'*40)
#     seperator.pack()

searchbar = tkinter.Entry()
searchbar.pack()

def search():
    searchquery = searchbar.get()
    
    search_results = api.search(q="hello", count=100)

    for tweet in search_results:
    # Do Whatever You need to print here
        tweettext = tweet.text.encode('ascii', 'ignore').decode('ascii')

        tweetLabel = tkinter.Label(root, text=tweettext)
        tweetLabel.pack()

        seperator = tkinter.Label(root, text='-'*40)
        seperator.pack()

searchbutton = tkinter.Button(root, text='Search.', command=search)
searchbutton.pack()
    
root.mainloop()