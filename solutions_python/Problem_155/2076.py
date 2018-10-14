'''
	Google Code Jam - Standing Ovation
'''

import sys
import re

file = open(sys.argv[1])

T = int(next(file).rstrip())

for case in range(T):
	
	audience = [ int(i) for i in list(next(file).rstrip().split(' ')[1]) ] 

	friends = 0

	while not all(i is 0 for i in audience[1:]):
		for ii, member in enumerate(audience):
			if ii is 0: continue
			if audience[0] >= ii:
				audience[0] += audience[ii]
				audience[ii] = 0
		if not all(i is 0 for i in audience[1:]):
			friends += 1
			audience[0] += 1
		
	print("Case #%i: %i" % (case + 1, friends))
