#! /bin/python

from math import sqrt, ceil, floor
import time as t
 
def time(f, *args):
	start = t.time()
	apply(f, list(args))
	return t.time() - start

def palindrome(nb):
	return str(nb)==str(nb)[::-1]

def find_all(a,b):
	n=0
	start = int(ceil(sqrt(a)))
	end = int(floor(sqrt(b)))+1
	
	for i in xrange(start, end):
		if palindrome(i) and palindrome(i*i):
			n += 1
			print str(i*i)
		i+=1

	return str(n)


data=open("data", "r")
out=open("out", "w")

size = int(data.readline())
for i in range(size):
	bounds = data.readline().split()

	result = find_all(int(bounds[0]), int(bounds[1]))

	out.write("Case #"+str(i+1)+": " + result+"\n")

data.close()
out.close()