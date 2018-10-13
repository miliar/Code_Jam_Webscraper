import sys
import os
import math

def getFairSquareCount(interval):
	res=0
	
	minmax = interval.split(" ")
	minmax[0] = int(minmax[0])
	minmax[1] = int(minmax[1])

	for i in range(minmax[0], minmax[1]+1):
		if isFairSquare(i):
			res += 1

	return res


def isFairSquare(numb):
	res = False

	if isPalindrome(numb):
		sq = math.sqrt(numb)
		if int(math.floor(sq)*math.floor(sq)) == numb:
			if isPalindrome(sq):
				res = True
	
	return res
	
	
def isPalindrome(numb):
	res = True

	
	nm = str(int(numb))
	indx = int(len(nm)/2)
	if not len(nm)%2 == 0:
		indx += 1

	for i in range(indx):
		if not nm[i] == nm[len(nm)-i-1]:
			res = False
			break
	
	return res
	


inp = ""
with open('c.out', 'w') as fo:

	with open(sys.argv[1], 'r') as fi:
		caseno = int(fi.readline())

		for i in range(caseno):
			line = fi.readline().strip()

			fo.write("Case #"+str(i+1)+": "+str(getFairSquareCount(line))+"\n")
			
		fi.closed

	fo.closed






