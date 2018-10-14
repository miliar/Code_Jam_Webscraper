#!/usr/bin/python
# Google Code Jam 2012 - Qualification Round - Problem B - Mateusz Kurek

import io

t = int(input())
for i in range(1,t+1):
	line = [int(value) for value in input().split()]
	n, s, p, *results = line
	atLeastP = 0
	maybeSupprising = 0

	for res in results:
		#get unequivocal decomposition result to r1,r2,r3 with no score that are more apart than 2
		r1 = int(res/3) # always min
		r2 = int((res-r1)/2)
		r3 = res-r1-r2 # always max
		if r3 >= p:
			atLeastP += 1
		elif r3 == p-1 and r2 > 0 and r2 == r3:
			maybeSupprising += 1
	#print(atLeastP, maybeSupprising)
	atLeastP += min(maybeSupprising, s)
	print("Case #{0}: {1}".format(i, atLeastP))
