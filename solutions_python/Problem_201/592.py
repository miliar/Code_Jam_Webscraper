#!/usr/bin/env python3
import sys
from collections import defaultdict
def ri():
    return map(int, sys.stdin.readline().split())


T = int(input())

a = defaultdict(int)

def sol(n, k):
    count = 0
    c1 = 1
    c2 = 0
    n1 = n
    n2 = 0
    while True:
        n1n = 0
        n2n = 0
        c1n = 0
        c2n = 0
        if c1 != 0:
            n1 = n1-1
            count += c1
            if k  <= count:
                if n1%2:
                    return(n1//2+1, n1//2)
                else:
                    return(n1//2, n1//2)
            if n1%2:
                c1n += c1
                c2n += c1
                n1n = n1//2+1
                n2n = n1//2
            else:
                c1n += c1*2
                n1n = n1//2
                n2n = n1//2-1
        else:
            pass

        if c2 != 0:
            n2 = n2-1
            count += c2
            if k  <= count:
                if n2%2:
                    return(n2//2+1, n2//2)
                else:
                    return(n2//2, n2//2)
            if n2%2:
                c1n += c2
                c2n += c2
                n1n = n2//2+1
                n2n = n2//2
            else:
                c2n += c2*2
                n1n = n2//2+1
                n2n = n2//2

        else:
            pass

        n1 = n1n
        n2 = n2n
        c1 = c1n
        c2 = c2n



for i in range(T):
    n, k = ri()
    ans = sol(n, k)

    print("Case #%d:"%(i+1), *ans)
