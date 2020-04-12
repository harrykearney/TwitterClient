import tkinter

root = tkinter.Tk()
root.title('TwitterClient Login.')
root.geometry('960x540')

title = tkinter.Label(root, text='Login.', font=('Arimo', 30))
title.pack()

consumer_key_entry = tkinter.Entry(root)
consumer_secret_entry = tkinter.Entry(root)
access_token_key_entry = tkinter.Entry(root)
access_token_secret_entry = tkinter.Entry(root)

consumer_key_entry.pack()
consumer_secret_entry.pack()
access_token_key_entry.pack()
access_token_secret_entry.pack()

def login():
    consumer_key =  consumer_key_entry.get()
    consumer_secret = consumer_secret_entry.get()
    access_token_key = access_token_key_entry.get()
    access_token_secret = access_token_secret_entry.get()

    with open('credentials.py', 'a+') as credentialsFile:
        print(f"consumer_key = '{consumer_key}'", file=credentialsFile)
        print(f"consumer_secret = '{consumer_secret}'", file=credentialsFile)
        print(f"access_token_key = '{access_token_key}'", file=credentialsFile)
        print(f"access_token_secret = '{access_token_secret}'", file=credentialsFile)
        
    successLabel = tkinter.Label(root, text='Success!', fg='green')
    successLabel.pack()

loginButton = tkinter.Button(root, text='Login', command=login)
loginButton.pack()

root.mainloop()