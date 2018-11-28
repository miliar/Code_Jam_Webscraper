import sys
import fileinput
import re

#fileio
#fileName = 'D-large'
fileName = 'D-small-attempt1'
#fileName = 'D-test'
input = fileName + ".in"
output = fileName + ".out"

# Richard will choose a omino as hard to fit as possible
# Gabriel can choose where to place the omino Richard chooses
# XRC <= 4
def fit(X,R,C):
	# If Richard and find a piece extends outside the region
	if R*C == X and X > 2: return False, 'exact'
	# If the rectangle is not dividable by X
	if (R*C)%X != 0: return False, 'mod'
	# If the board is narrow enough to make a T shaped omino
	if X >= 4 and (C == 2 or R == 2): return False, 'T'
	return True, 'good'
  
###
with open(input) as fi, open(output, "w") as fo:
	count = 0
	for line in fi.readlines()[1:]:
	#	print line
		result = True
		###
		X,R,C = map(int, line.split(' '))
		result = 'GABRIEL' if fit(X,R,C)[0] else 'RICHARD'
		#normal
		count += 1
		resultStr = "Case #"+str(count)+": "+str(result)
		print resultStr
		fo.write(resultStr+'\n')

