#! /usr/bin/python
import re
import string

def readinp():
	global dict1
	global p
	global case

	f = open("inpfile","r")
	firstline = f.readline().strip("\n")
	wordlen = int(firstline.split()[0])
	totalWords = int(firstline.split()[1])
	numofTests = int(firstline.split()[2])
	
	dict1 = []
	j = 0
	while (j < totalWords):
		j = j+1
		line = f.readline().strip("\n")
		dict1.append(line)
	
	case = 0

	for line in f.readlines():
		case = case + 1
		regexp1 = line.strip("\n")
		regexp1 = regexp1.replace("(","[").replace(")","]")
		regexp1 = "^" + regexp1 + "$"
		p = re.compile(regexp1)
		countwords()

def countwords():
	count = 0
	for i in dict1:
		m = p.match(i)
		if m:
			count = count + 1

	print "Case #" + str(case) + ": " + str(count)

readinp()
