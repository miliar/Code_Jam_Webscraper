#!/usr/bin/env python3

# Solution to Problem C. Fair and Square in Python 3.

from bisect import bisect_left, bisect_right

fsnos = [1, 4, 9]

def evenstore(ar):
    global fsnos
    i = int(''.join(ar + list(reversed(ar))))
    fsnos += [i * i]

def oddstore(ar):
    global fsnos
    i = int(''.join(ar[:-1] + list(reversed(ar))))
    fsnos += [i * i]

for n in range(2, 51):
    if n % 2 == 0:
        hn = n // 2
        ar = ['0'] * hn
        ar[0] = '1'
        evenstore(ar)
        for i in range(hn-1, 0, -1):
            ar[i] = '1'
            evenstore(ar)
            for j in range(hn-1, i, -1):
                ar[j] = '1'
                evenstore(ar)
                for k in range(hn-1, j, -1):
                    ar[k] = '1'
                    evenstore(ar)
                    ar[k] = '0'
                ar[j] = '0'
            ar[i] = '0'
        ar[0] = '2'
        evenstore(ar)
    else:
        hn = n // 2 + 1
        ar = ['0'] * hn
        ar[0] = '1'
        oddstore(ar)
        ar[hn-1] = '1'
        oddstore(ar)
        ar[hn-1] = '2'
        oddstore(ar)
        ar[hn-1] = '0'
        for i in range(hn-2, 0, -1):
            ar[i] = '1'
            oddstore(ar)
            ar[hn-1] = '1'
            oddstore(ar)
            ar[hn-1] = '2'
            oddstore(ar)
            ar[hn-1] = '0'
            for j in range(hn-2, i, -1):
                ar[j] = '1'
                oddstore(ar)
                ar[hn-1] = '1'
                oddstore(ar)
                ar[hn-1] = '0'
                for k in range(hn-2, j, -1):
                    ar[k] = '1'
                    oddstore(ar)
                    ar[hn-1] = '1'
                    oddstore(ar)
                    ar[hn-1] = '0'
                    ar[k] = '0'
                ar[j] = '0'
            ar[i] = '0'
        ar[0] = '2'
        oddstore(ar)
        ar[hn-1] = '1'
        oddstore(ar)

for c in range(int(input())):
    a, b = [int(s) for s in input().split()]
    i = bisect_left(fsnos, a)
    j = bisect_right(fsnos, b)
    print("Case #{}: {}".format(c+1, j - i))
