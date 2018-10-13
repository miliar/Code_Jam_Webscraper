
# coding: utf-8

# In[3]:

import numpy as np
import itertools as it


# In[77]:

def solve(*args):
    print(args)


# In[129]:

class I(BaseException):
    pass

import functools

@functools.lru_cache(maxsize=None)
def mini_solve(N, K):
    assert K != 0
    
    if K == N:
        return (0,0)
    
    odd = N % 2
    
    if K == 1:
        if odd:
            return (N // 2, N // 2)
        
        return (N//2, N//2 -1)
    
    kodd = (K - 1) % 2
    
    if not kodd:
        if odd:
            return mini_solve(N //2, (K - 1) // 2)
        
        return mini_solve(N //2 - 1, (K - 1) // 2)
    
    # K-1 is odd
    if odd:
        return mini_solve(N //2, (K - 1) // 2 + 1)
    
    return mini_solve(N //2, (K - 1) // 2 + 1)
    

def solve(N, K):
    s = mini_solve(N, K)
    return '{} {}'.format(s[0], s[1])


# In[123]:

solve(1000,1), solve(1000,1000), solve(10,3)


# In[104]:

(3,2) > (4,1)


# In[131]:

path = r'C:\Users\Shachar\Downloads\C-small-1-attempt0.in'
with open(path, 'r') as f, open(path[:-2]+'out', 'w') as outf:
    T = int(f.readline())
    for test_index in range(T):
        N, K = (int(x) for x in f.readline().split())
        outf.write('Case #{}: {}\n'.format(test_index+1, solve(N,K)))

