import random
from string import *
import webbrowser
import os

letters = 'abcdefghijklmopqrstuvwxyz' #make the first list of letters
letters = letters + upper(letters) #combine the first string with uppercase string

url = 'http://i.imgur.com/' #url name for imgur
for i in range(5): #use this loop to get five random letters
	url = url +random.choice(letters)

webbrowser.open(url) #open a broswer with the imgur page



