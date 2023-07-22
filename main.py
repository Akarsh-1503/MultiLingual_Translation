import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
import pyttsx3



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
    summary.config(state='disabled')
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

root= tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

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

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
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


btn = tk.Button(root, text="Speech", command= speech)
btn.pack()

root.mainloop()