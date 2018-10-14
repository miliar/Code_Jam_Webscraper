#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 00:26:32 2017

@author: shuzheng
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 21:15:08 2017

@author: shuzheng
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:54:02 2017

@author: shuzheng
"""
import itertools


def checkifsorted(l):
    return all(earlier <= later for earlier, later in itertools.izip(l, l[1:]))



def solve(n):

    numlist = list(str(n[0]))
    if len(numlist) < 2:
        return int(numlist[0])
    
    numlist_int = list(map(int, numlist))
    uniquenumlist_int = set(numlist_int)
    if len(uniquenumlist_int) == 1:
        return n[0]
    
    numlist_int = list(map(int, numlist))
    num = long(n[0])
    

    
    for i in reversed(xrange(num+1)):
        numlist = list(str(i))
        numlist_int = list(map(int, numlist))
        
        #if max(numlist_int[1:]) >= numlist_int[0]:
            #print i, max(numlist_int[1:])
            #continue
        #print i, max(numlist_int[1:])
        if checkifsorted(numlist_int):
            return i
        
        #if monotonic(numlist_int):
        #    return i
        
        #if non_decreasing(numlist_int):
        #    return i
    
    return i



if __name__ == "__main__":
    
    """The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S, each character of which is either + (which represents a pancake that is initially happy side up) or - (which represents a pancake that is initially blank side up). The string, when read left to right, represents the stack when viewed from top to bottom."""
    T = int(raw_input())
    for i in xrange(1, T+1):
        n = [s for s in raw_input().split(" ")] #$f.readline().strip()
        solution = solve(n)
        print("Case #{0}: {1}".format(i, solution))