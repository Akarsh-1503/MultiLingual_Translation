import tkinter as tk
from tkinter import ttk
from tkinter import *
import nltk
from textblob import TextBlob
from newspaper import Article
import pyttsx3
from googletrans import Translator, LANGUAGES



def summarize():
    
    url= utext.get('1.0', "end").strip()
    # nltk.download('punkt')

    # url = 'http:// timesofindia.indiatimes.com/world/china/chinese-expert-warns-of-troops-entering-kashmir/articleshow/59516912.cms'

    article= Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    
    author.delete('1.0', 'end')
    if article.authors != [] :
        author.insert('1.0', article.authors)
        # print("check")
        print(article.authors)
    else:
        author.insert('1.0', "Not Available")
        print(article.authors)
    # author.insert('1.0', article.authors)

    
    publication.delete('1.0', 'end')
    if article.publish_date != None :
        publication.insert('1.0', article.publish_date)
        # print("check")
        # print(article.publish_date)
    else:
        publication.insert('1.0', "Not Available")
        

    
    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis= TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity >0 else "negative" if analysis.polarity<0 else "neutral"}')
    # print(f'Sentiment: {"positive" if analysis.polarity >0 else "negative" if analysis.polarity<0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    # summary.config(state='disabled')
    sentiment.config(state='disabled')

    # print(f'Title: {article.title}')
    # print(f'Authors: {article.authors}')
    # print(f'Summary: {article.summary}')


def speech():
    url= utext.get('1.0', "end").strip()
    # nltk.download('punkt')

    # url = 'http:// timesofindia.indiatimes.com/world/china/chinese-expert-warns-of-troops-entering-kashmir/articleshow/59516912.cms'

    article= Article(url)

    article.download()
    article.parse()

    article.nlp()
    text_speech= pyttsx3.init()
    answer= article.summary
    text_speech.say(answer)
    text_speech.runAndWait()


def change(text="type", src="english", dest="hindi"):
    text1= text
    src1= src
    dest1= dest
    trans= Translator()
    trans1= trans.translate(text1, src1, dest1)
    return trans1.text

def data():
    url= utext.get('1.0', 'end').strip()
    # nltk.download('punkt')

    # url = 'http:// timesofindia.indiatimes.com/world/china/chinese-expert-warns-of-troops-entering-kashmir/articleshow/59516912.cms'

    article= Article(url)

    article.download()
    article.parse()

    article.nlp()

    s= combo_sor.get()
    d= combo_dest.get()
    msg= article.summary
    # print("message")
    # print(msg)
    textGet= change(text=msg, src=d, dest=s)
    # print("output")
    # print(textGet)
    summary.delete(1.0, END)
    summary.insert(END, textGet)


#     button_change= Button(frame, text="Translate", )
root= tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')
root.config(bg='#ADD8E6')

# frame= Frame(root).pack(side=BOTTOM)
# sor_txt= Text(frame, font=("Times New Roman", 20, "bold"), wrap=WORD)

list_text= list(LANGUAGES.values())

sor_txt= Text(root)
sor_txt.place(x=0,y=550, height=30, width=150)
combo_sor= ttk.Combobox(root, value=list_text)
combo_sor.place(x=300,y=550, height=30, width=150)
combo_sor.set("english")

button_change= Button(root, text="Translate", relief=RAISED, command= data)
button_change.place(x=530,y=550, height=30, width=150)

dest_txt= Text(root)
dest_txt.place(x=900,y=550, height=30, width=150)
combo_dest= ttk.Combobox(root, value=list_text)
combo_dest.place(x=740,y=550, height=30, width=150)
combo_dest.set("english")

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()



alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()



plabel = tk.Label(root, text="Publication")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()



slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=16, width=140)
summary.config(state='normal', bg='#dddddd')
summary.pack()


selabel = tk.Label(root, text="Sentiment")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()


ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize", command= summarize)
btn.pack()


btn = tk.Button(root, text="Speak", command= speech)
btn.pack()

# btn = tk.Button(root, text="Translate", command= translator)
# btn.pack()


root.mainloop()