#this is an albhed to english translator
#need to add english to al- bhed
#Final Fantasy x credit to Square Enix for the language

# a-e, b-p, c-s, d-t, e-i, f-w, g-k, h-n, i-u
# j-v, k-g, l-c, m-l, n-r, o-y, p-b, q-x, r-h
# s-m, t-d, u-o, v-f, w-z, x-q, y-a, z-j

import string


#Translate from al-bhed
def english(c):
	c = string.lower(c) # Lower case for simplicity
	if c == 'a': return 'e'
	elif c == 'b': return 'p'
	elif c == 'c': return 's'
	elif c == 'd': return 't'
	elif c == 'e': return 'i'
	elif c == 'f': return 'w'
	elif c == 'g': return 'k'
	elif c == 'h': return 'n'
	elif c == 'i': return 'u'
	elif c == 'j': return 'v'
	elif c == 'k': return 'g'
	elif c == 'l': return 'c'
	elif c == 'm': return 'l'
	elif c == 'n': return 'r'
	elif c == 'o': return 'y'
	elif c == 'p': return 'b'
	elif c == 'q': return 'x'
	elif c == 'r': return 'h'
	elif c == 's': return 'm'
	elif c == 't': return 'd'
	elif c == 'u': return 'o'
	elif c == 'v': return 'f'
	elif c == 'w': return 'z'
	elif c == 'x': return 'q'
	elif c == 'y': return 'a'
	elif c == 'z': return 'j'
	elif c == ' ': return " "

#Translate into albhed
def albhed(c):
	c = string.lower(c) # Lower case for simplicity
	if c == 'e': return 'a'
	elif c == 'p': return 'b'
	elif c == 's': return 'c'
	elif c == 't': return 'd'
	elif c == 'i': return 'e'
	elif c == 'w': return 'f'
	elif c == 'k': return 'g'
	elif c == 'n': return 'h'
	elif c == 'u': return 'i'
	elif c == 'v': return 'j'
	elif c == 'g': return 'k'
	elif c == 'c': return 'l'
	elif c == 'l': return 'm'
	elif c == 'r': return 'n'
	elif c == 'y': return 'o'
	elif c == 'b': return 'p'
	elif c == 'x': return 'q'
	elif c == 'h': return 'r'
	elif c == 'm': return 's'
	elif c == 'd': return 't'
	elif c == 'o': return 'u'
	elif c == 'f': return 'v'
	elif c == 'z': return 'w'
	elif c == 'q': return 'x'
	elif c == 'a': return 'y'
	elif c == 'j': return 'z'
	elif c == ' ': return " "

#Function for translation	
def translate(phrase, language):
	string =""
	for c in phrase:
		if language == "english":
			string = string + english(c)
		else:
			string = string + albhed(c)	
	return string




