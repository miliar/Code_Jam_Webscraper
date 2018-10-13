#!/usr/bin/python

import sys

vowels = ['a', 'e', 'i', 'o', 'u']


def count(s, minlen):
	w = ""
	cnt = []

	for i in s:
		if i in vowels:
			w = ""
		else:
			w += i
			if len(w) == minlen:
				cnt += [w]
				w = ""

	return cnt
		

cases = int(sys.stdin.readline())

data = "\n"
for case in range(1, cases+1):
	data = sys.stdin.readline()
	if data == None:
		break

	data = data.split(' ')
	if len(data) != 2:
		break

	word = data[0]
	sublen = int(data[1][:len(data[1])-1])
	

	concons = []

	for i in range(0, len(word)-sublen+1):
		for j in range(len(word)-i, sublen-1, -1):
#			print "testing substring ", i, j
			if i+j > len(word):
				print "FAILED"

			subword = word[i:][:j]
			c = count(subword, sublen)
#			print subword, len(c)

			if len(c) == 0:
				break
			else:
				concons += [(i,j,c)]
		

#		subword = word[::-1][i:]
#		concons += count(subword, sublen)
#		print subword, len(concons)

	print "Case #%i: %i" % (case, len(concons))
	
		


#	print case
#	print word
#	print sublen


	
