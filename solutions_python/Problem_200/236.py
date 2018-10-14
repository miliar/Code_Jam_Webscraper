#!/usr/bin/env python3

# Tatiana has OCB

# N is an integer or a string describing a number
def last_tidy(N):
    "return last tidy number before N"
    N = [d for d in str(N)]
    last,j = '0',-1
    for i,d in enumerate(N):
        if d < last:
            N[j] = str(int(N[j])-1)
            N[j+1:] = ['9']*(len(N)-(j+1))
        elif d > last:
            last,j = d,i
    return int(''.join(N))

import sys
file=sys.stdin

n = int(file.readline()) # number of cases
for i in range(1, n+1):
    N = int(file.readline()) # beware of the '\n'

    T = last_tidy(N)

    print("Case #%d: %d" % (i,T))
