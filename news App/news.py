import requests

import pyttsx3 
def Topnews():
    
   my_api_key="9d5327103dc6417c833edb5ed4729ebc"

   my_url = "https://newsapi.org/v2/top-headlines?category=technology&country=in&apiKey="+my_api_key+"&pageSize=10"
   
   newsinjson = requests.get(my_url).json()
   
   my_article = newsinjson["articles"]
   
   my_results = []
   
   for title in my_article:
      my_results.append(title["title"])
      
   return my_results

      
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

   
   
