import pyshorteners
# Taking url input
url = input("Enter your url here : ")
# creating a function
def shortner(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))
# calling shortner function
shortner(url)