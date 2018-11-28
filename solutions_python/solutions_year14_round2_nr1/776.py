#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import math
import sys

def countBeginChar(s, c):
    count = 0
    for cc in s:
        if cc == c:
            count=count+1
        else:
            break
    return count

if __name__ == "__main__":
    t = input()
    for caseIdx in xrange(1,t+1):
    	#n, l = map(int, raw_input().split(' '))
        n = input()
        s=[]
        for i in xrange(n):
            s.append(raw_input())

        ans = 0
        while len(s[0])!=0:
            c = s[0][0]
            count = []
            for idx in xrange(n):
                if len(s[idx])==0 or s[idx][0]!=c:
                    ans = -1
                    break
                num_c = 0
                while len(s[idx])!=0 and s[idx][0] == c:
                    num_c = num_c + 1
                    s[idx] = s[idx][1:]
                count.append(num_c)
            if ans == -1:
                break
            avg = round(sum(count)/n)
            ans = ans + sum(map(lambda v: abs(v-avg), count))

        for ss in s:
            if len(ss)!=0:
                ans = -1

        if ans != -1:
            print "Case #%d: %d" % (caseIdx, ans)
        else:
            print "Case #%d: Fegla Won" % (caseIdx)
