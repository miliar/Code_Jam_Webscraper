import numpy as np
import pandas as pd
import re
out = []
df = pd.read_csv('A-large.in',header=None,index_col=None)

N = int(df.values[0][0])

for i in xrange(1,N+1):
	s = df.values[i][0]
	pancakes, flipper = s.split()
	K = int(flipper)
	#pancakes = list(pancakes)
	#last = list('')
	#lastt= list('')
	last = ''
	lastt= ''
	steps = 0
	while True:
		#lastt = list(''.join(last))
		#last = list(''.join(pancakes))
		##
		lastt = last
		last = pancakes
		foo = re.search(r'-',''.join(pancakes))
		##
		if foo is not None:
			steps = steps+1
			s = foo.start()
			if s+K > len(pancakes):
				out.append( 'Case #' + str(i) + ': IMPOSSIBLE')
				break
			
			for k in range(K):
				pancakes = list(pancakes)
				if ord(pancakes[s+k]) == ord('-'):
					pancakes[s+k]='+'
				else:
					pancakes[s+k]='-'
				pancakes = ''.join(pancakes)
		else:
			out.append('Case #' + str(i) + ': ' + str(steps))
			break
		#if ''.join(pancakes)==''.join(lastt):
		if pancakes == lastt:
			out.append( 'Case #' + str(i) + ': IMPOSSIBLE')
			print 'aaah'
			break

with open("mout.txt", "w") as text_file:
	for line in out:
		text_file.write(line + "\n")
