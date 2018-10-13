
# coding: utf-8

# In[ ]:




# In[2]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

from __future__ import division
import time, random, re, copy , pickle
from operator import itemgetter


# In[ ]:




# In[47]:

#reading file
file_name = 'A-large.in'
f = open(file_name,'r')

N = int(f.readline())

l = []
for _ in range(N):
    tmp = f.readline()
    l.append(tmp.split(" ")[1][:-1])


# In[48]:

l
cc = []
for s in l:
    b = 0
    c = 0
    while s<>'':
        
        if s[0] <> '0':
            b += int(s[0])
            s = s[1:]
            b += -1
        else:
            if b+c > 0:
                b += -1
                s = s[1:]
            else:
                c += 1
                b += -1
                s = s[1:]
            
    cc.append(c)


# In[49]:

#writing file

out = open('out_A-large.txt','w')
for i,c in enumerate(cc):
    #print('Case #' + str(i+1) + ': ' + str(g(S,li)))
    out.write('Case #' + str(i+1) + ': ' + str(c) + '\n')
    
out.close()

