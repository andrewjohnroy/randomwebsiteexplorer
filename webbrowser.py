import webbrowser
import random
file = open("/usr/share/dict/words", "r")
list = []
for line in file:
    list.append(line)

webbrowser.open("http://www." + list[random.randint(0,len(list))][0:-3] + ".com")
