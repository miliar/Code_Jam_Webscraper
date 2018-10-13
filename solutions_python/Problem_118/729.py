from math import *

def isPalin(s):
	s = str(s)
	a = s[:len(s)/2]
	b = s[(len(s)+1)/2:]
	return a == ''.join(reversed(b))

def makePalin(n):
	s1 = str(n)
	s1 += '0'*len(s1)
	s2 = str(n)[:-1]
	s2 += '0'*(len(s2)+1)
	return [int(s1)+int(''.join(reversed(s1))), int(s2)+int(''.join(reversed(s1)))]

def solve(A):
	total = 0
	cur = 1
	#plist = []
	while True:
		palins = makePalin(cur)
		if palins[1]*palins[1] > A:
			break
		for i in reversed(palins):
			i2 = i*i
			if isPalin(i2) and i2 <= A:
				total += 1
				#plist.append(i)
		cur += 1
	#plist.sort()
	#print plist
	return total

T = int(raw_input())
for t in xrange(1, T+1):
	A, B = [int(i) for i in raw_input().split()]
	print "Case #%d: %d"%(t, solve(B)-solve(A-1))

