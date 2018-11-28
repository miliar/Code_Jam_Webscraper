#!/usr/bin/python
import sys

def mainfunc():
	f = open("input.txt", "r")
	i = int(f.readline().strip())
	j = 0
	n = 0
	while (j < i):
		(a,b) = [int(x) for x in f.readline().strip().split()]
		n = a;
		count = 0
		while (n <= b):
			ml = list(str(n))
			mlen = len(ml)
			mcount = 0;
			while (mcount < mlen):
				ml.insert(0, ml[-1])
				ml.pop()
				m = int("".join(ml))
				if (n == m):
					break
				if ((n < m and m <= b)):
					count += 1
				mcount += 1
			n += 1
		print "Case #%d: %d" % (j+1, count)
		j += 1
	
if __name__ == "__main__":
	mainfunc()
