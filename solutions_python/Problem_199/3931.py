#!/usr/bin/python3

import sys
sys.setrecursionlimit(30)

flip = lambda c: '+' if c=='-' else '-'

def flipping_pancakes(s, k, flips=0):    
    try:
        l = s.index('-')
    except ValueError:
        return flips
    else:
        try:
            r = s[::-1].index('-')
            if l <= r:
              s[l:l+k] = list(map(flip, s[l:l+k]))
            else:
              r = abs(r - len(s))
              s[r-k:r] = list(map(flip, s[r-k:r]))
            flips += 1
            return flipping_pancakes(s,k,flips)
        except RecursionError:
          #raise
          return 'IMPOSSIBLE'
          

test_ct = int(input())
i = 1
while True:
    try:        
        params = input().split()
        if len(params) == 2:
            s, k = list(params[0]), int(params[1])
            print("Case #{}: {}".format(i, flipping_pancakes(s, k)))
        else:
            k = int(params[0])
            print("Case #{}: {}".format(i, k))
        i += 1
    except Exception:
        break

