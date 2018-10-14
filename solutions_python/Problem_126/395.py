#!/usr/bin/env python

import sys

cons = "bcdfghjklmnpqrstvwxyz"
vows = "aeiou"

def getSubstr(string, limit):
    for start in xrange(len(string)):
        for end in xrange(len(string) + 1):
            if start + limit <= end:
                yield string[start:end]
            #endif
        #endfor
    #ednfor
#enddef

def solve(name, n):
    retval = 0
    for substr in getSubstr(name, n):
        conLen = 0
        for letter in substr:
            if letter in vows:
                conLen = 0
            else:
                conLen += 1
            #endif
            if conLen >= n:
                retval += 1
                break
            #endif
        #endfor
    #endfor
    return retval
#enddef

def main():
	T = int(sys.stdin.readline())
	for caseNumber in xrange(1, T+1):
	    name, n = sys.stdin.readline().split()
	    print "Case #%d: %d" % (caseNumber, solve(name, int(n)))
	#endfor
#enddef

if __name__ == '__main__':
	main()
#endif


