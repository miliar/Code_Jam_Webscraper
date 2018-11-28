#!/usr/bin/env python

import sys


def get():
    row = sys.stdin.readline().split(" ")
    sMax = int(row[0])
    s = []
    for i in range(0, sMax + 1):
        if i < len(row[1]):
            s.append(int(row[1][i]))
        else:
            s.append(1)

    return sMax, s


def solve():
    sMax, s = get()
    standing = 0
    needed = 0
    
    for shyness, one in enumerate(s):
        if standing < shyness:
            needed += shyness - standing
            standing += shyness - standing

        standing += one    
    
    return needed
    

def main():
	T = int(sys.stdin.readline())
	for caseNumber in xrange(1, T+1):
	    print "Case #%d: %s" % (caseNumber, solve())


if __name__ == '__main__':
	main()

