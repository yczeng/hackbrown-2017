'''
import os, sys, subprocess

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])
'''

import subprocess, os, time
import webbrowser
import string
import urllib
import urllib2
from bs4 import BeautifulSoup
from evdev import uinput, ecodes as e

process = subprocess.Popen("/home/yczeng/Documents/HackBrown/iochat/runserver/0runserver", stdout=subprocess.PIPE)
process2 = subprocess.Popen("/home/yczeng/Documents/HackBrown/iochat/runserver/1mobile")

while True:
    while True:
        out = str(process.stdout.readline())
        if (out[0:4] == "ppp "):
            print(out[4:])
            command = out[4:]
            command = command.lower()
            print(command)

            search_index = command.find('search')

            search = command.replace(" ", "+")
            print(search)
            search_term = search[(search_index+6):]
            search_term = search_term[:-1]
            print(search_term)


            if (command.find("browser") != -1):
                process3 = subprocess.Popen("/home/yczeng/Documents/HackBrown/iochat/runserver/2browser")
            if (command.find("youtube") != -1):
                webbrowser.open_new("https://www.youtube.com/results?search_query=" + search_term)

                textToSearch = search_term
                query = urllib.quote(textToSearch)
                url = "https://www.youtube.com/results?search_query=" + query
                response = urllib2.urlopen(url)
                html = response.read()
                soup = BeautifulSoup(html)
                with open("Output.txt", "w") as text_file:
                    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
                        text_file.write('https://www.youtube.com' + vid['href'] + '\n')
                        print 'https://www.youtube.com' + vid['href']

                with open("Output.txt", "r") as ins:
                    array = []
                    for line in ins:
                        array.append(line)

            if (command.find("video one") != -1):
                webbrowser.open_new(array[0])

            if (command.find("close") != -1):

                control_f4_sequence = '''keydown key N
                key N
                                keyup key N'''
                
                def keypress(sequence):
                    p = subprocess.Popen(['xte'], stdin=subprocess.PIPE)
                    p.communicate(input=sequence)
                keypress(control_f4_sequence)

            if (command.find("presentation") != -1):
                process5 = subprocess.Popen("/home/yczeng/Documents/HackBrown/iochat/runserver/4presentation")

            if (command.find("google") != -1):
                webbrowser.open_new("https://www.google.com/#q=" + search_term)



