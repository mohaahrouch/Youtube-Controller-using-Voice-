# import time
# import speech_recognition as sr
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager  # Importing ChromeDriverManager
# import pyttsx3

# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak("MyBot is listening...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
#     try:
#         command = recognizer.recognize_google(audio).lower()
#         return command
#     except sr.UnknownValueError:
#         return "Sorry, I couldn't understand what you said."
#     except sr.RequestError:
#         return "Sorry, there was an issue with the speech recognition service."

# def speak(text, rate=200, volume=0.8, voice_id=None):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', rate)
#     engine.setProperty('volume', volume)
#     if voice_id:
#         engine.setProperty('voice', voice_id)
#     engine.say(text)
#     engine.runAndWait()

# def open_youtube(driver):
#     driver.get("https://www.youtube.com/")
#     return driver

# def search(driver, query):
#     try:
#         search_box = driver.find_element_by_css_selector("input#search")
#         search_box.clear()
#         search_box.send_keys(query)
#         search_box.send_keys(Keys.RETURN)
#     except Exception as e:
#         print("Error occurred while searching:", e)
#         speak("Sorry, I encountered an error while searching.")
#         return

# def choose_video(driver, number):
#     videos = driver.find_elements_by_id("video-title")
#     videos[number - 1].click()

# if __name__ == "__main__":
#     options = webdriver.ChromeOptions()   
 
#     d = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())


#     bot_name = "MoBot"
#     speak(f"{bot_name}: {bot_name} is ready.")
#     print(f"{bot_name}: {bot_name} is ready.")
#     command = listen()
#     speak(f"You said: {command}", rate=150, volume=0.9)
#     print(f"You: {command}")

#     if "youtube" in command:
#         driver = open_youtube(d)
#         speak(f"{bot_name}: YouTube opened. What do you want to search for?")
#         print(f"{bot_name}: YouTube opened. What do you want to search for?")
#         search_query = listen()
#         speak(f"You said: {search_query}")
#         print(f"You: {search_query}")
#         search(driver, search_query)
#         time.sleep(3)
#         speak(f"{bot_name}: Here are the search results. Which video do you want to choose?")
#         print(f"{bot_name}: Here are the search results. Which video do you want to choose?")
#         choice = listen()
#         speak(f"You said: {choice}")
#         print(f"You: {choice}")
#         if "scroll" in choice:
#             driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
#             speak(f"{bot_name}: Scrolled.")
#             print(f"{bot_name}: Scrolled.")
#             time.sleep(2)
#         elif "choose video number" in choice:
#             number = int(choice.split()[-1])
#             choose_video(driver, number)
#             speak(f"{bot_name}: Video number {number} chosen.")
#             print(f"{bot_name}: Video number {number} chosen.")
#         else:
#             speak(f"{bot_name}: Sorry, I couldn't understand your choice.")
#             print(f"{bot_name}: Sorry, I couldn't understand your choice.")
#     else:
#         speak(f"{bot_name}: Sorry, I can only open YouTube right now.")
#         print(f"{bot_name}: Sorry, I can only open YouTube right now.")


import time
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager  # Importing ChromeDriverManager
import pyttsx3
from selenium.webdriver.common.by import By


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("MyBot is listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        return command
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError:
        return "Sorry, there was an issue with the speech recognition service."

def speak(text, rate=200, volume=0.8, voice_id=None):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    if voice_id:
        engine.setProperty('voice', voice_id)
    engine.say(text)
    engine.runAndWait()

def open_youtube():
    options = webdriver.ChromeOptions()   
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Set your Chrome binary location here
    
    driver  = webdriver.Chrome(options=options)
    driver.get("https://www.youtube.com/")
    return driver

def search(driver, query):
    try:
        search_box = driver.find_element(By.CSS_SELECTOR,"input#search")
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
    except Exception as e:
        print("Error occurred while searching:", e)
        speak("Sorry, I encountered an error while searching.")
        return

def choose_video_by_title(driver, title):
    videos = driver.find_elements(By.CSS_SELECTOR,"#video-title")
    for video in videos:
        if title.lower() in video.text.lower():
            video.click()
            speak(f"{bot_name}: Video '{title}' chosen.")
            print(f"{bot_name}: Video '{title}' chosen.")
            return True
    speak(f"{bot_name}: Sorry, couldn't find a video with the title '{title}'.")
    print(f"{bot_name}: Sorry, couldn't find a video with the title '{title}'.")
    return False


def controll_video(driver,cmd):
    if "pause" in cmd:
        pause_button = driver.find_element(By.CSS_SELECTORL,"#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button")
        pause_button.click()
    if "move"  in cmd:
        video = driver.find_element(By.CSS_SELECTORL,"#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button")
        scroll_duration_seconds = 10 
        video.send_keys(Keys.ARROW_RIGHT * scroll_duration_seconds)
    if "back"  in cmd:
        video = driver.find_element(By.CSS_SELECTORL,"#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button")
        scroll_duration_seconds = 10 
        video.send_keys(Keys.ARROW_LEFT * scroll_duration_seconds)
                        
    if "full screen" in cmd:
        fs = driver.find_element(By.CSS_SELECTOR,"#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-fullscreen-button.ytp-button")
        fs.click()
    if "exit full screen "in cmd:
        efs = driver.find_element(By.CSS_SELECTOR,"#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-fullscreen-button.ytp-button")
        efs.click()
    
    if "like" in cmd:
        like = driver.find_element(By.CSS_SELECTOR,"#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill")
        like.click()
    
    if "dislike" in cmd:
        dislike = driver.find_element(By.CSS_SELECTOR,"#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > dislike-button-view-model > toggle-button-view-model > button-view-model > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill")
        dislike.click()
        
    if "subscribe" in cmd:
        subscribe = driver.find_element(By.CSS_SELECTOR,"#subscribe-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill")
        subscribe.click()
        
    
    


        

        
if __name__ == "__main__":


    bot_name = "MooBot"
    speak(f"{bot_name}: {bot_name} is ready.")
    print(f"{bot_name}: {bot_name} is ready.")
    command = listen()
    speak(f"You said: {command}", rate=150, volume=0.9)
    print(f"You: {command}")

    if "youtube" in command:
        driver = open_youtube()
        speak(f"{bot_name}: YouTube opened. What do you want to search for?")
        print(f"{bot_name}: YouTube opened. What do you want to search for?")
        search_query = listen()
        speak(f"You said: {search_query}")
        print(f"You: {search_query}")
        search(driver, search_query)
        time.sleep(2)
        speak(f"{bot_name}: Here are the search results. Which video do you want to choose?")
        print(f"{bot_name}: Here are the search results. Which video do you want to choose?")
        choice = listen()
        speak(f"You said: {choice}")
        print(f"You: {choice}")
        if "scroll" in choice:
            driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
            speak(f"{bot_name}: Scrolled.")
            print(f"{bot_name}: Scrolled.")
            time.sleep(2)
        elif "choose video" in choice:
            title = choice.replace("choose video", "").strip()
            choose_video_by_title(driver, title)
            cmd = listen()
            speak(f"You said: {choice}")
            print(f"You: {choice}")
            controll_video(driver,cmd)
        else:
            speak(f"{bot_name}: Sorry, I couldn't understand your choice.")
            print(f"{bot_name}: Sorry, I couldn't understand your choice.")
    else:
        speak(f"{bot_name}: Sorry, I can only open YouTube right now.")
        print(f"{bot_name}: Sorry, I can only open YouTube right now.")
