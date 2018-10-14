#!/usr/bin/python
import sys

input = sys.argv[1]
#output = sys.argv[2]

input = open(input).read().strip().split("\n")

cases = int(input[0].strip())

result = ""
for i in range(0,cases):
	item = input[i+1].strip().split(" ")
	cElements = {}
	oElements = {}
	strings = []
	
	c = int(item[0])
	for j in range(0,c):
		element = item[1+j][0:-1]
		cElements[element] = item[1+j][-1]
	
	d = int(item[c+1])
	for j in range(0,d):
		chars = item[c+2+j]
		if chars[0] in oElements:
			oElements[chars[0]].append(chars[1])
		else:
			oElements[chars[0]] = []
			oElements[chars[0]].append(chars[1])
		if chars[1] in oElements:
			oElements[chars[1]].append(chars[0])
		else:
			oElements[chars[1]] = []
			oElements[chars[1]].append(chars[0])

	
	string = item[c + d + 3]
	elements = []
	for c in string:
		if len(elements) == 0:
			elements.append(c)
		else:
			_c = elements[-1]
			s1 = c+_c
			s2 = _c+c
			if s1 in cElements:
				elements[-1] = cElements[s1]
			elif s2 in cElements:
				elements[-1] = cElements[s2]
			else:
				elements.append(c)
				if c in oElements:
					for oc in oElements[c]:
						if oc in elements:
							elements = []
							break
	outstr = "["
	for e in elements:
		outstr += e + ", "
	if len(outstr) > 1:
		outstr = outstr[:-2]
	outstr += "]"
	print "Case #"+str(i+1)+": " + outstr 
