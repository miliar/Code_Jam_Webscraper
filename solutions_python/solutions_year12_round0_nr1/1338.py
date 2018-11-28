import re

key = {' ': ' ', 'q': 'z','a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c',
 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b',
 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a',
 'x': 'm', 'z': 'q'}

f1=open("in.txt","r")
cases = []

for line in f1:
	if re.match("^\d*$",line):
		continue
	cases.append(line.strip())
	
case=0
	
for line in cases:
	case = case+1
	string =""
	for letter in line:
		string = string + key[letter]
	String = "Case #"+str(case)+": "+string
	print String