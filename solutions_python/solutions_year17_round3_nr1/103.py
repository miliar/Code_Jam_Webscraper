from math import *

def func(n,k,l):
    #print(l,k)
    
    l.sort(reverse=True)
    ll = []
    for i in l:
        h = i[0]
        r = i[1]
        s = 2*r*pi*h
        ll.append((s,r))
    ll.sort(reverse=True)
    Max = 0

    #print(ll)
    for (ii,i) in enumerate(ll):
        #print(i)
        r = i[1]
        lll = []
        for (jj,j) in enumerate(ll):
            if ii == jj:
                continue
            if j[1] <= r:
                lll.append(j)
        if len(lll) < k-1:
            continue
        lll.sort(reverse=True)
        #print(lll)
        #print(' --- ', [ss[0] for ss in lll[:k-1]])
        area = pi*r**2 + sum([ss[0] for ss in lll[:k-1]]) + i[0]
        if area > Max:
            Max = area
    return Max

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n,k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    l = []
    for j in range(n):
        r,h = [float(f) for f in input().split(" ")]
        l.append((h,r))
    print("Case #{}: {}".format(i, func(n,k,l)))
