#codejam code question 1 

#+-+-+++-+-++
#++-+-++-+-++
#++-+-+-+-+++
#+++-+--+-+++
#+++--++--+++
#+++++----+++
#++++++++++++

#+-+-+++-+-++
#++-+-++-+-++
#+++-+-+-+-++
#++++-+--+-++
#+++++-+++-++
#++++++----++
#++++++++++++

#+-+-+++-+-++
#++-+-++-+-++
#+++-+-+-+-++
#++++-+--+-++
#+++++-+++-++
#++++++----++
#++++++++++++

#+++--++-+---
#+++++---+---
#++++++++----
#++++++++++++

#++-----+--+
#++++++-+--+
#+++++++-+++

import sys
import math


def convert(letter): 
	if letter == "+": 
		return "-"
	else:
		return "+"

if __name__ == "__main__":

	filename = sys.argv[1]
	with open(filename) as f: 
		content = f.readlines()
		content = [x.strip() for x in content] 
	#print content

	argcount = int(content[0])
	#sprint argcount


	for cot in xrange(1, argcount+1, 1):
		word = []
		number = 0
		#print cot
		for i in xrange(len(content[cot])): 
			if content[cot][i] != " ":
				word.append(content[cot][i])
			else: 
				digits = len(content[cot])-i-1
				for j in xrange(digits): 
					#print j
					number += int(content[cot][i+j+1])*pow(10, digits-j-1)
				break

		#print word, number

		s = word		
		klen = int(number)
		flag = True
		flag2 = True

		length = len(s)
		count = 0 

		temp = int(length-klen+1)

		for i in xrange(temp):
			#print s
			if s[i] != "+": 
				for l in xrange(klen):
					s[i+l] = convert(s[i+l])

				
				count += 1
			flag = True	

			for j in xrange(length):
				if s[j] != "+":
					flag = False

			#print flag
			
			if flag == True: 
				flag2 = False
				break
			
				



		if flag2 == True: 
			print "Case #%s: %s" % (cot, "IMPOSSIBLE")
		else: 
			print "Case #%s: %s" % (cot, count)







