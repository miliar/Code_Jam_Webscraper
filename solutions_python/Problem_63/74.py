"""
python 2.6.x program by Ji Han
"""

import sys
from math import *

def f(L,P,C):
	return int(ceil(log(ceil(log(ceil(P/float(L)),C)),2)))
def main():
	T = int(sys.stdin.readline())
	for k in range(1, T + 1):
		line = sys.stdin.readline()
		L, P, C = map(int, line.split())
		print "Case #%d: %d" % (k, f(L, P, C))

if __name__=='__main__': 
        main()
