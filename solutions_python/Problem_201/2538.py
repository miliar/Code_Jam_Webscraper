t = int(input()) 
try:
    N,K = zip(*[el for el in [list(map(int,input().split())) for i in range(t)]])
# if more than 2 numbers per line, no error, simply discarded
except Exception:
    print('incorrect format')
    exit()

import numpy as np
def calc(n,k):
    l = np.array([0,n+1]) # indices of occupied stalls (1..n)
    def set_k(l):
        ld = np.diff(l)
        loc=ld.argmax()
        index=ld[loc] // 2
        l = np.insert(l,loc+1,l[loc]+index)
        ls = l[loc+1] - l[loc] - 1
        rs = l[loc+2] - l[loc+1] - 1
        return l,ls,rs

    for i in range(k):
        l,ls,rs = set_k(l)
#        print(ls,rs,l)
    return max(ls,rs),min(ls,rs)

for i in range(t):
    y,z = calc(N[i],K[i])
    print ('Case #{}: {} {}'.format(i+1,y,z))

