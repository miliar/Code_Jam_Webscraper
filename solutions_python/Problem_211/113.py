#!/usr/bin/env python

#from Math import round

def can_achive(mid,Cores,U):
	mysum = 0
	for c in Cores:
		if (c<mid):
			mysum += (mid - c)
	if (mysum > U):
		return 0
	return 1

def mybest(Cores,limit):
	if (Cores[0] < limit):
		best = limit
	else:
		best = Cores[0]
	for x in xrange(1,len(Cores)):
		if (Cores[x] < limit):
			best *= limit
		else:
			best *= Cores[x]
	return best

def solve():
	N , K = [int(i) for i in raw_input().split()]
	U = float(raw_input())
	Cores = [float(i) for i in raw_input().split()]
	#Cores.sort()
	#Cores.reverse()
	#Cores = Cores[:K]
	bottom = min(Cores)
	limit = 1.0
	while(limit>bottom + 0.00000001):
		mid = bottom + (limit - bottom) / 2
		#print "limit: {} , bottom: {} , mid: {}".format(limit,bottom,mid)
		#if (limit == 1.5): 
		#	break
		ret = can_achive(mid,Cores,U)
		if (ret == 1):
			bottom = mid
		else:
			limit = mid
	return mybest(Cores,limit)

def main():
    T = int(raw_input())
    for t in xrange(T):
    	sol = solve()
    	print "Case #" + str(t + 1) + ": " + "{0:.6f}".format(round(sol,6))

if __name__ == '__main__':
	main()