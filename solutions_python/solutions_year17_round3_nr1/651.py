import numpy as np
import itertools

def calc_area(s):
    ret=sum(2*np.pi*x[0]*x[1] for x in s)
    ret+=sum(np.pi*(s[i+1][0]**2-s[i][0]**2) for i in range(len(s)-1))
    return ret+s[0][0]**2*np.pi

def radius(p):
    return p[0]
def solve(n,k,pancakes):
    ret=-1
    for ind in itertools.combinations(range(n),k):
        tmp=[]
        for i in range(k):
            tmp.append(pancakes[ind[i]])
        tmp.sort(key=radius)
        tmp2=calc_area(tmp)
        ret=max([ret,tmp2])
    return ret

t=int(input())
for i in range(1,t+1):
    n,k=[int(x) for x in input().split(' ')]
    pancakes=[]
    for _ in range(n):
        pancakes.append([int(x) for x in input().split()])
    print('Case #{0}: {1}'.format(i,solve(n,k,pancakes)))
        
        
