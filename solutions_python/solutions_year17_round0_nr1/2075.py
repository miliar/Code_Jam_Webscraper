from operator import xor
from functools import reduce
from itertools import product

def solve(s,M):
    N=len(s)
    b=[t=='+' for t in s]
    min_=N+1

    edge=N-M

    for ops in product((0,1),repeat=edge+1):
        #print(ops)
        res=[]

        for i in range(N):
            now=reduce(xor,ops[max(0,i-M+1):min(i,edge)+1])
            #print(i,now)
            res.append(now ^ b[i])

        if all(res): min_=min(min_,sum(ops))
        #import pdb;pdb.set_trace()

    return 'IMPOSSIBLE' if min_>N else min_

K=int(input())

for i in range(K):
    s,M=input().split()

    print('Case #{}: {}'.format(i+1,solve(s,int(M))))
        
