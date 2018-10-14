#!/usr/bin/python

import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        (A,N) = map(int, sys.stdin.readline().split())
        motes = map(int, sys.stdin.readline().split())
        if A == 1:
            print "Case #" + str(t+1) + ": " + str(len(motes))
            continue
        motes.sort()
        numOps = [float("inf")] * len(motes)
        prev = 0
        for i in range(len(motes)):
            if A > motes[i]:
                A += motes[i]
            else:
                ops = 0
                while A <= motes[i]:
                    A += (A-1)
                    ops += 1
                A += motes[i]
                if ops >= len(motes)-i:
                    numOps[i] = prev + len(motes) - i
                    break
                else:
                    prev += ops
            numOps[i] = prev + len(motes) - i - 1
        print "Case #" + str(t+1) + ": " + str(min(numOps))
            
            
