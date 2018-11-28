# -*- coding: utf-8 -*-

def calc(N, P):
	m = 2**N
	if P == m:
		return m
	if P >= m//2:
		return m - 1
	else:
		return 2 * calc(N - 1, P) - 1

if __name__ == "__main__":
    s = open("B-large.in.txt", "r")
    f = open("outputB.txt", "w")
    for i in range(int(s.readline())):
    	N, P = map(int, s.readline().split())
    	M = 2**N
    	if P == M:
    		resy = M - 1
    	else:
	    	resy = M - calc(N, M - P) - 1
    	resz = calc(N, P) - 1
    	print (resy, resz)
    	print ('Case #{0}: {1} {2}'.format(i+1, resy, resz), file=f)
    f.close()
