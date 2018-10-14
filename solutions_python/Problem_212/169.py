from math import *

def func(n,p,l):
    r = 0
    ll = []
    for g in l:
        if g % p == 0:
            r += 1
        else:
            ll.append(g)
    l = ll

    if p == 2:
        r+=ceil(len(l)/2)

    elif p == 3:
        n1 = 0
        n2 = 0
        for g in l:
            if g % 3 ==1:
                n1 += 1
            else:
                n2 += 1
        #print(n1,n2)
        h = min((n1,n2))
        r += h
        n1 -= h
        n2 -= h

        if n1 == 0:
            n = n2
        else:
            n = n1
        while n > 2:
            r += 1
            n -= 3

        if n != 0:
            r += 1

    else:
        n1 = 0
        n2 = 0
        n3 = 0
        for g in l:
            if g % 4 ==1:
                n1 += 1
            elif g % 4 == 2:
                n2 += 1
            else:
                n3 += 1
        while n2 > 1:
            r += 1
            n2 -=2
        while n3 > 0 and n1 > 0:
            r += 1
            n1 -= 1
            n3 -= 1
        if n3 == 0:
            n = n1
        else:
            n = n3
        while n2 > 0 and n > 1:
            r+=1
            n2 -= 1
            n -= 2
        while n > 3:
            r += 1
            n -= 4
        if n > 0 or n2 > 0:
            r += 1
    return r

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n,p = [int(s) for s in input().split()]
    l = [int(s) for s in input().split()]
    #print(n,r,o,y,g,b,v)
    print("Case #{}: {}".format(i, func(n,p,l)))
