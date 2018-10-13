
# coding: utf-8

# In[ ]:




# In[1]:

"""
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

from __future__ import division
import time, random, re, copy , pickle
from operator import itemgetter
from math import *
"""
from math import *


# In[ ]:




# In[12]:

#reading file
file_name = 'B-large.in'

f = open(file_name,'r')

N = int(f.readline())

ll = []
for _ in range(N):
    f.readline()
    tmp = f.readline()
    ll.append(map(int,tmp.split(" ")))


# In[13]:

def all_under(l,x):
    
    lx = map(lambda p: int((p-1)/x), l)
    s = sum(lx)
    
    return s + x

def tmin_bf(l):
    
    lt = [max(l)]
    for x in range(2,max(l)+1):
        lt.append(all_under(l,x))
    return min(lt)


# In[14]:

#ll_large = [ [1000]*5 , [100]*2, [100] * 3 ] * 100


# In[15]:

t = []
#ll = ll_large

for l in ll:
    t.append(tmin_bf(l))


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[16]:

#writing file

out = open('out_B.txt','w')
for i,z in enumerate(t):
    #print('Case #' + str(i+1) + ': ' + str(g(S,li)))
    out.write('Case #' + str(i+1) + ': ' + str(z) + '\n')
    
out.close()


# In[ ]:



