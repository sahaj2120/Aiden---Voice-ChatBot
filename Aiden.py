import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
s = input("Enter Whom Do You Want To Interact:\n 1 ----> Girl \n 2 ----> Boy \n")
if s == "1":
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Aiden, Your Personal Assistant. Please tell me how may I help you")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("I am Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Sorry! I Was Unable To Catch That Can You Please Say that again...")
        return "None"
    return query


driver = webdriver.Chrome(
    executable_path='C:\\Users\\Sahaj Patel\\Downloads\\ChromeDriv\\chromedriver.exe')


def openYoutube():
    speak("Please Speak What Do You Want to search on youtube")
    searchh = takeCommand()
    speak(f'Searching Youtube For: {searchh}')

    driver.get("https://www.youtube.com/")

    searchBox = driver.find_element_by_xpath('//*[@id="search"]')
    searchBox.send_keys(searchh)

    searchButton = driver.find_element_by_xpath(
        '//*[@id="search-icon-legacy"]')
    searchButton.click()
    speak(f"Successfully Searched Youtube For {searchh}")

# End of searching youtube:

# Opening And Searching For Google:


def googleSearch():
    speak("Please Speak What Do You Want To Search On Google")
    searchh01 = takeCommand()
    speak(f"Searching Google For: {searchh01}")

    driver.get("https://www.google.com/")

    searchQuery = driver.find_element_by_xpath(
        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    searchQuery.send_keys(searchh01)

    searchButton01 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
    searchButton01.click()
    speak(f"Succesfully Searched Google for {searchh01}")

# End Of Google Search

# # Unsplash Login


def unsplash():
    speak("Opening Unsplash")
    driver.get("https://unsplash.com/")
    speak("Do you want me to log you in on unsplas?")
    response = takeCommand()
    if response.lower() == "yes":
        speak("Trying To Login on unsplash..")

        login = driver.find_element_by_xpath(
            '//*[@id="app"]/div/header/nav/div[3]/div/div[2]/a[1]')
        login.click()

        emaillogin = driver.find_element_by_xpath('//*[@id="user_email"]')
        speak("Entering Email")
        emaillogin.send_keys("yourmail@gmail.com")

        passlogin = driver.find_element_by_xpath('//*[@id="user_password"]')
        speak("Entering Password")
        passlogin.send_keys("XXXXXXXXXXXX")

        login01 = driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/div/form/div[3]/input')
        login01.click()

        speak("Succesfully Logged In On Unsplash")

    else:
        speak("Thanks For Your Response.")

# # End Of Unsplash Login

# Searching Google Maps


def gmaps():
    speak("Opening Google Maps")

    speak("Please Speak The Name Of Place You Want To Search")
    place = takeCommand()
    speak(f"Searching Google Maps For: {place}")

    driver.get("https://www.google.com/maps")

    searchboxx = driver.find_element_by_xpath('//*[@id="searchboxinput"]')
    searchboxx.send_keys(place)

    searchbuttonn = driver.find_element_by_xpath(
        '//*[@id="searchbox-searchbutton"]')
    searchbuttonn.click()
    speak("{place} was searched succesfully")

# End Of Searching Google Maps

# Search On Amazon


def amazonSearch():
    speak("Opening Amazon India")
    speak("Please Speak The Name Of Item You Want To Search")
    item = takeCommand()
    speak(f"Searching Amazon India For: {item}")

    driver.get("https://www.amazon.in/")

    itemSearch = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
    itemSearch.send_keys(item)

    itemButton = driver.find_element_by_xpath(
        '//*[@id="nav-search-submit-button"]')
    itemButton.click()
    speak(f"Successfully Searched Amazon India For {item}")

# End Of Amazon Search


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            openYoutube()

        elif 'open world of sahaj' in query:
            speak("Opening worldofsahaj")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("https://worldofsahaj.netlify.app/")

        elif 'open google' in query:
            googleSearch()

        elif 'open stackoverflow' in query:
            speak("Opening Stackoverflow")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("stackoverflow.com")

        elif 'open gmail' in query:
            speak("Opening Gmail")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("gmail.com")

        elif 'open link' in query:
            speak("Opening Programming In C Link")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(
                "https://meet.google.com/wap-qvnj-rya")

        elif 'open unsplash' in query:
            unsplash()

        elif 'open facebook' in query:
            speak("Opening FaceBook")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("facebook.com")

        elif 'open instagram' in query:
            speak("Opening Instagram")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("instagram.com")

        elif 'open amazon' in query:
            amazonSearch()

        elif 'open flipkart' in query:
            speak("Opening Flipkart")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("flipkart.com")

        elif 'open maps' in query:
            gmaps()

        elif 'open whatsapp' in query:
            speak("Opening Whatsapp In The Browser")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("https://web.whatsapp.com/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"User, the time is {strTime}")

        elif 'open code' in query:
            speak("Opening Code")
            codePath = "C:\\Users\\Sahaj Patel\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'how are you' in query:
            speak(
                "I am fine! Thank You For Asking.I hope you and your loved ones are safe and healthy.")

        elif 'who are you' in query:
            speak("I am aiden and I am your personal assistant")

        elif 'sem result' in query:
            speak("Opening Semister 1 Result")
            codePath = "C:\\Users\\Sahaj Patel\\Desktop\\ITM\\DOCUMENTS\\SEM1_RESULT.pdf"
            os.startfile(codePath)

        elif 'delete' in query:
            speak("Oh Ho! It seems I don't have Permission To Do That")

        elif 'your name' in query:
            speak("My name is Aiden")

        elif 'are sweet' in query:
            speak("You are sweet too")

        elif 'siri or google' in query:
            speak('It seems like a wrong question. Nobody Can Beat Me!')

        elif 'who made you' in query:
            speak("I was developed by Sahaj Patel")

        elif 'bye' in query:
            speak("It was nice talking to you. Byeeee")
            break

        elif 'old are you' in query:
            speak("I have always wanted to do this. How old do you think I am?")
            takeCommand()
            speak("Intresting...what makes you think that?")
            takeCommand()
            speak("Okay that's quite a guess...do you wanna know how old i actually am?")
            age = takeCommand()
            if age == "Yes":
                speak("I was developed in 2021, so techincally I'm pretty young.")
            else:
                speak("Okay.You can ask me something else..")

        elif 'what is my name' in query:
            speak("Your Name Is Sahaj, Sir")

        elif 'can you dance' in query:
            speak("Sorry I don't Know How to Dance.")

        elif 'exit' in query:
            speak("Hope I Helped You!")
            speak("Exiting The Programm")
            break
