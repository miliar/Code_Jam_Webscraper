#!/usr/bin/python
import math
total = 0
def check(v,mi,ma):
	global total
	b = str(v ** 2)
	c = b[::-1]
	if (int(b) > ma):
		 return 0
	if (int(b) < mi):
		 return 0
	if (b == c):
		total += 1

def gen(a,mi,ma,l1,l2):
	val = 0
	for i in xrange(1,10):
		v = int(str(i) + str(a) + str(i))
		if (v > ma):
			return 0
		gen(v,mi,ma,l1,l2)
		if (v < mi):
			continue;
		check(v,l1,l2)
		


def get_nums(a):
	max_val = int(math.sqrt(int(a[1])))
	min_val = int(math.sqrt(int(a[0])))
	for i in xrange(0,10):
		check(i,int(a[0]),int(a[1]))
		gen(i,min_val,max_val,int(a[0]),int(a[1]))
	gen('',min_val,max_val,int(a[0]),int(a[1]))
	return total






f = open("input.txt", "r")
inp = []
for i in f:
	i = i.rstrip()
	inp.append(i.split(' '))

num_cases = int(inp[0][0])
for i in xrange(1,num_cases+1):
	total = 0
	print "Case #%d: %d" % (i, get_nums(inp[i]))
