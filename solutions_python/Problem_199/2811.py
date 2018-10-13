import sys
import os


def getminflips(r , k):
	p = [x for x in r]
	flips = 0
	possible = True
	limit = len(p) - k
	for i , s in enumerate(p):
		if s=='-':
			if i > limit:
				possible = False
				break
			flips =  flips + 1
			for m in range(i , i+k):
				if p[m] == '+':
					p[m] = '-'
				else:
					p[m] = '+'

	if possible:
		return flips
	else:
		return 'IMPOSSIBLE'




no_of_cases = int(raw_input())
# print "Number of test cases: {0}".format(no_of_cases)

testcases = []
for n in range(no_of_cases):
	l = raw_input().split(" ")	
	testcases.append(( l[0] , int(l[1]) ))


# print testcases

for index , value  in enumerate(testcases):
	print "Case #{0}: {1}".format(index+1 , getminflips(testcases[index][0] , testcases[index][1]))



