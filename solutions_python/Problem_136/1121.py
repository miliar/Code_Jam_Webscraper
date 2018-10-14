#!/usr/bin/env python

import sys


def solve():
    C, F, X = list(float(one) for one in sys.stdin.readline().split(" "))
    Fcurr = 2.0
    timeSpent = 0.0
    
    while True:
        leftTimeToX = X / Fcurr
        leftTimeToXwithBuy = (C / Fcurr) + (X / (Fcurr + F))
        if leftTimeToX < leftTimeToXwithBuy:
            timeSpent += leftTimeToX
            break
        else:
            timeSpent += (C / Fcurr)
            Fcurr += F
        #endif
    #endwhile
    
    return timeSpent
#enddef

def main():
	T = int(sys.stdin.readline())
	for caseNumber in xrange(1, T+1):
	    print "Case #%d: %.7f" % (caseNumber, solve())
	#endfor
#enddef

if __name__ == '__main__':
	main()
#endif


