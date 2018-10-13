#!/usr/bin/env python

import sys

def calc(R, k, g):
    result = 0
    for i in range(R):
        ksum = 0
        
        for j in range(len(g)):
            if ksum + g[j] > k:
                j -= 1
                break;
            ksum += g[j]
        result += ksum
        newg = g[j+1:] + g[0:j+1]
        g = newg
 
    return result

def main():
    num = int(sys.stdin.readline().strip())
    for i in range(num):
        (R, k, N) = sys.stdin.readline().strip().split()
        g = sys.stdin.readline().strip().split()
        if len(g) != int(N):
            sys.stderr.write("mismatch\n")
        g = [int(x) for x in g]
        result = calc(int(R), int(k), g)
        print "Case #%d: %d" % (i+1, result)

if __name__ == '__main__':
    main()
