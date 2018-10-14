#!/usr/bin/python3
import sys,os
from itertools import count

def main():
    def line():
        return sys.stdin.readline().strip()
    T = int(line())
    for trial in range(T):
        Smax, s = line().split(' ')
        Smax = int(Smax)
        assert Smax+1==len(s)
        S = dict((i,int(c)) for i,c in zip(count(),s))
        standing_so_far = 0
        extra_needed = 0
        for i in range(0,Smax+1):
            if standing_so_far < i:
                extra_needed += (i-standing_so_far)
                standing_so_far = i
            standing_so_far += S[i]
        print("Case #{:d}: {:d}".format(trial+1,extra_needed))

main()
