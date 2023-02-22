from urllib.request import urlopen
import re
import time 
sleep = time.sleep

print("File reader! Automatically read through any txt doc/docx or PDF document\nNo skipping! No stopping! Finish the text!\n")

location = None 
query_web = input("Is it on the web or is it saved on your computer? (WEB/COMPUTER) ").lower()
if query_web == "web":
    print("Selected: web")
    location = input("Where is it on the web? (LINK) ")
elif query_web == "computer":
    print("Selected: computer")
    location = input("Where is it on your device? (LOCATION) ")
else:
    raise Exception("Failed. Please enter a value that is 'web' or 'computer', '" + query_web + "' is not a valid value.")

print("Ok. Just two more questions.")

lines_per = int(input("How many lines should appear at once? (TIMES) "))
occurance = int(input("How often should it appear? (SECONDS) "))

def text():
    if query_web == "web":
        print("Ok. It's a web file at " + location)
        data = urlopen(location)
        return data
    elif query_web == "computer":
        print("Ok. It's a local file at " + location)
        out = open(location, "r")
        out = out.readlines()
        return out

def print_text(text):
    i=0
    for line in text: 
        i+=1  
        line = str(line)
        line = line[2:(len(line) - 3)]
        print(line)
        if i + 1 >= lines_per:
            i=0
            sleep(occurance) 

            
print("\nPreparing...\n")
print("'" + location + "':\n\n")
print_text(text())
