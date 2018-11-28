#!/usr/bin/env python
import sys
from bisect import bisect_left
import string

X = [1, 4, 9]

def check(n):
	if n == n[::-1]:
		m = str(int(n)*int(n))
		if m == m[::-1]:
			X.append(int(m))
			return

def odd_recur(depth, length, curr):
	if length == 0:
		check(curr + '0' + curr[::-1])
		check(curr + '1' + curr[::-1])
		check(curr + '2' + curr[::-1])		
		return
	if depth > 0:
		odd_recur(depth-1, length-1, curr+"1")
	odd_recur(depth, length-1, curr+"0")
		
def even_recur(depth, length, curr):
	if length == 0:
		check(curr + curr[::-1])
		return
	if depth > 0:
		even_recur(depth-1, length-1, curr+"1")
	even_recur(depth, length-1, curr+"0")
		
def odd(n):
	odd_recur(3, n-1, "1")

def even(n):
	even_recur(3, n-1, "1")


for d in xrange(2, 101):
	if d % 2 == 1:
		odd(int(d/2))
		check("2" + "0"*(d-2) + "2")
		check("2" + "0"*int((d-2)/2) + "1" + "0"*int((d-2)/2) + "2")
	else:
		even(int(d/2))
		check("2" + "0"*(d-2) + "2")

X.sort()

T = int(sys.stdin.readline())

for tt in xrange(T):
	A, B = [int(x) for x in sys.stdin.readline().split()]
	cnt = 0
	pos = bisect_left(X, A)
	for i in xrange(pos, len(X)):
		if X[i] >= A and X[i] <= B:
			cnt += 1
		if X[i] > B:
			break
		
	print "Case #%d: %d" % (tt + 1, cnt)
