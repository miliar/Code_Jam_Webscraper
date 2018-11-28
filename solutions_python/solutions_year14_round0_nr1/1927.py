#!/usr/bim/env python

import sys

f = open(sys.argv[1])
g = open('output.txt','w')
n = int(f.readline().strip())
for i in xrange(n):
	row = int(f.readline().strip())
	cards = []
	for j in xrange(4): 
		cards.append( [int(k) for k in f.readline().strip().split()] )
	subset_1 = cards[row-1]

	row = int(f.readline().strip())
	cards = []
	for j in xrange(4): 
		cards.append( [int(k) for k in f.readline().strip().split()] )
	subset_2 = cards[row-1]

	matches = 0
	for j in subset_1:
		if j in subset_2:
			matches += 1
			k = j

	output = "Case #"+str(i+1)+': '
	if matches == 1:
		output += str(k)
	elif matches > 1:
		output += 'Bad magician!'
	else:
		output += 'Volunteer cheated!'

	g.write(output+'\n')
f.close()
g.close()
