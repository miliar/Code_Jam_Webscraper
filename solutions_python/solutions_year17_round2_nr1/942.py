
# coding: utf-8

# In[42]:

#mode = 'practice'
#mode = 'small'
mode = 'large'
problem = 'A'
attempt = '0'


# In[43]:

import numpy as np
if mode == 'practice':
    infile = 'input.txt'
    outfile = 'output.txt'
if mode == 'small':
    infile = problem+'-small-attempt'+attempt+'.in'
    outfile = problem+'-small.out'
if mode == 'large':
    infile = problem+'-large.in'
    outfile = problem+'-large.out'
f = open(infile, 'r')
lines = f.readlines()
f.close()
cases = int(lines[0].rstrip())
outputfile = open(outfile, 'w')
pos = 0


# In[44]:

def solve(D,N,K,S):
    latest = 0.0
    for i in range(N):
        time = (float(D)-float(K[i]))/float(S[i])
        if time > latest:
            latest = time
    return str(float(D)/float(latest))


# In[45]:

for i in range(cases):
    pos= pos+1
    nums = lines[pos].rstrip().split(" ")
    D = int(nums[0])
    N = int(nums[1]) 
    K=[]
    S=[]
    for j in range(N):
        pos = pos+1
        nums2 = lines[pos].rstrip().split(" ")
        K.append(int(nums2[0]))
        S.append(int(nums2[1]))
    out = "CASE #" + str(i+1) + ": " + solve(D,N,K,S)
    outputfile.write(out)
    outputfile.write("\n")


# In[46]:

outputfile.close()


# In[ ]:




# In[ ]:



