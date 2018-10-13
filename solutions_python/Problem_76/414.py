#!/usr/bin/env python

def solveCase(N,C):
	if reduce(lambda x,y:x^y, C) != 0:
		return "NO"
	else:
		C.sort()
		return str(sum(C[1:]))

def main():
	T = input()

	for i in range(T):
		N = input()
		C = [int(j) for j in raw_input().split()]
		print "Case #%d: %s" % (i+1, solveCase(N, C))
	
	return

main()

