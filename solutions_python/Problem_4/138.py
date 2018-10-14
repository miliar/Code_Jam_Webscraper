#! /usr/bin/python

def multiply(a, b):
	return a*b

fp = open("input_a.txt", "r")
numCases = int(fp.readline())
for i in range(numCases):
	vLen = int(fp.readline())
	v1 = map(int, fp.readline().rstrip("\n").split(' '))
	v2 = map(int, fp.readline().rstrip("\n").split(' '))

	v1 = sorted(v1)
	v2 = sorted(v2)
	v2.reverse()
	ans = reduce(lambda x, y: x+y, map(multiply, v1, v2))
	print "Case #%d: %d" % (i+1, ans) 

	
