import requests
import pyttsx3 
import tkinter as tk
from tkinter import ttk
root = tk.Tk()

root.title("Sparking News")

root.geometry('600x400')

root.minsize(600, 400)
root.attributes('-topmost', 1)

label = tk.Label(root, text ="Welcome to Sparking News !").pack()

def Topnews():
        
        my_api_key="9d5327103dc6417c833edb5ed4729ebc"

        my_url = "https://newsapi.org/v2/top-headlines?category=technology&country=in&apiKey="+my_api_key+"&pageSize=10"
        
        newsinjson = requests.get(my_url).json()
        
        my_article = newsinjson["articles"]
        
        my_results = []
    
        for title in my_article:
            my_results.append(title["title"])
            tk.Label(root, text =title["title"],borderwidth="6").pack(pady="10")
            
        return my_results

ttk.Button(root, text='news',command=Topnews).pack()

def main():      
    if __name__ == '__main__':
        
        
            

        j=1
        engine = pyttsx3.init()
        engine.setProperty("rate", 120)
        engine.say("Top 10 technology headlines by skysparko")

            
        for i in range(10):
            
            
            engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')   
            
            engine.say("Today's number")
            engine.say(j)
            engine.say("News is")
            engine.setProperty("rate", 120)
            engine.say(Topnews()[i])
            
            engine.runAndWait()
            j+=1

        
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
        engine.setProperty("rate", 120)
        engine.say("Thank you for using sparking news see you tommorow with more fresh news , Bye!")
        engine.runAndWait()
        engine.stop()

   


ttk.Button(root, text='Read for me',command=main).pack()

root.mainloop()