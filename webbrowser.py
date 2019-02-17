#!/usr/bin/env python3
import webbrowser
import random
file = open("/usr/share/dict/words", "r")
list = []
for line in file:
    if "\'" not in line:
        list.append(line)

hostname = list[random.randint(0,len(list))]

webbrowser.open("http://www." + hostname + ".com")
