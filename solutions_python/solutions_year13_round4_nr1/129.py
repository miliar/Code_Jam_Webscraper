#!/usr/bin/env python
import sys
def cost(i, p, n):
	return i * (n + 1 -i + n) /2 * p
def optimize(arr, n, cur):
	# print >>sys.stdout, arr,cur
	if len(arr) == 0:
		return cur
	v = min(arr)
	arr = [ i - v for i in arr]
	cur += cost(len(arr), v, n)
	# print >>sys.stdout, arr, cur
	ind = [ i for i,x in enumerate(arr) if x == 0]

	ind.insert(0,-1)
	ind.append(len(arr))
	# print ind
	for i in xrange(1,len(ind)):
		# print i,ind[i-1]+1, ind[i]
		cur = optimize(arr[ind[i-1]+1:ind[i]], n, cur)
	return cur		

def main():
	count = int(raw_input())
	for case in xrange(1, count+1):
		(stops, lines) = [int(i) for i in raw_input().split()]
		pairs = []
		people = [0] * stops
		origin = 0
		for i in xrange(0,lines):
			(o,e,p) = [int(i) for i in raw_input().split()]
			for i in xrange(o, e): 
				people[i-1] += p
			origin += cost(e-o,p,stops)
			# print origin
		# print origin
		opt_cost = optimize(people, stops, 0)
		print "Case #%d: %d" %(case, origin - opt_cost)

main()


