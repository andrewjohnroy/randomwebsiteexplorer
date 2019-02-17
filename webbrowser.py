import webbrowser
import random
file = open("/usr/share/dict/words", "r")
list = []
for line in file:
    list.append(line)

while True:
    hostname = list[random.randint(0,len(list))]
    if "\'" not in hostname:
        break

webbrowser.open("http://www." + hostname + ".com")
