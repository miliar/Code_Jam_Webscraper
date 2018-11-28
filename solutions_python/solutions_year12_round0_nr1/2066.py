#!/usr/bin/env python
import sys
import fileinput

translationMap = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}


out = open('sampleOut.o', 'w')
# sample = open('Out.o', 'r')
# listofSample = []
# for line1 in sample:
# 	listofSample.append(line1)

# print listofSample
tMap = {'a':'y', 'o':'e','z':'q', 'q':'z'}
start = 1
T = 0
x=0
listOutputString = []
for line in fileinput.input():
	
	if start == 1:
		T = int(line.replace("\n",""))
		start = 0
	
	elif (not start and line != "\n"):
		# print "im here"
		# print line
		# print T
		
		G = line.split(' ')
		# print G
		# O = listofSample[x].split(' ')
			# print O
		i = 0
		listOutputString.append("Case #" + str(x+1) + ": ")
		for word in G:
			j=0
			word = word.replace("\n","")
			# print i
			# print O[i]
			# wordInO = O[i].replace("\n","")
			# print wordInO
				
			for letter in word:
					# print word
				listOutputString[x] += translationMap[letter]
				# tMap[letter] =  wordInO[j]

					# print tMap
				j+=1
			
			listOutputString[x] += " "

			i+=1
		out.write(listOutputString[x].strip() + "\n")
		x+=1


# k = 0
# for item in listOutputString:
# 	listOutputString[k] = item.strip()
# 	k+=1

# print listOutputString