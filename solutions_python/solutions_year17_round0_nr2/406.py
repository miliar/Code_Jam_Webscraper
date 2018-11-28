
# coding: utf-8

# In[3]:

import numpy as np
import itertools as it


# In[32]:

def solve(*args):
    print(args)


# In[66]:

class I(BaseException):
    pass

def solve(N):
    s = [int(c) for c in str(N)]
    
    if len(s) == 1:
        return N
    
    for i in range(len(s)):
        if i == len(s) - 1:
            return N
        
        if s[i] > s[i+1]:
            break
            
    return solve(int(str(N)[:i] + str(s[i] - 1) + '9'*(len(s) - i - 1)))


# In[69]:

solve(438),solve(10000),solve(7),solve(71),solve(129),solve(399),solve(999),solve(111), solve(110), solve(10), solve(109)


# In[73]:

for i in range(100):
    solve(10 ** 18 - 10*i)


# In[75]:

path = r'C:\Users\Shachar\Downloads\B-small-attempt0.in'
with open(path, 'r') as f, open(path[:-2]+'out', 'w') as outf:
    T = int(f.readline())
    for test_index in range(T):
        N = int(f.readline())
        outf.write('Case #{}: {}\n'.format(test_index+1, solve(N)))

