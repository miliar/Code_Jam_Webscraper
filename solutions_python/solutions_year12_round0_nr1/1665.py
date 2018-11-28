#!/usr/bin/python3


def translate(googletext):
	#key = letter in googlerese, value in english
	dictionnary = {'a':'y', 'b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}

	translated = str()
	for i in googletext:
		if i == ' ':
			translated += ' '
		else:
			translated += dictionnary[i]
	return translated

lines = list()
nb_lines = int(input())
for i in range(nb_lines):
	lines.append(input())

for i in range(nb_lines):
	print('Case #' + str(i+1) + ': ' + translate(lines[i]))
