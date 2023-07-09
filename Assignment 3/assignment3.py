from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigating to the YouTube homepage
driver.get("https://www.youtube.com")
time.sleep(3)

# Finding the search bar and entering text
search_bar = driver.find_element("name", "search_query")
search_bar.send_keys("Software Testing Methodologies")
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "Software Testing Methodologies" in driver.title
video_title_link = driver.find_element("xpath", "//a[@id='video-title']")
video_title_link.click()

# Waiting for the video page to load
time.sleep(5)

# Watching the video for five seconds
time.sleep(7)

# Navigating to the YouTube Trending page
driver.get("https://www.youtube.com/feed/trending")
time.sleep(5)

# Clicking on the first video in the trending list
first_video_link = driver.find_element("xpath", "//ytd-video-renderer[1]//a[@id='thumbnail']")
first_video_link.click()

# Waiting for the video page to load
time.sleep(5)

# Liking the video
like_button = driver.find_element("xpath", "//button[contains(@aria-label, 'like this video')]")
like_button.click()

# Waiting for the like button animation to complete
time.sleep(5)

# Clicking on the "Sign In" button
sign_in_button = driver.find_element("xpath","/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-modal-with-title-and-button-renderer/div/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]")
sign_in_button.click()

# Waiting for the sign-in page to load
time.sleep(5)

# Closing the webdriver
driver.close()
