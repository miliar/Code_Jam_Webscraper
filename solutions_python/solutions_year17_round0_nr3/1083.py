
# coding: utf-8

# In[14]:

#din = r'p3\samp.txt'
din = r'p3\C-small-1-attempt0.in'
#din = r'p3\C-large.in'
from math import *
with open(din, 'r') as f:
    inputs = f.readlines()


# In[15]:

results = []

for line in inputs[1:]:
    N, K = list(map(int, line.split()))
    k = int(floor(log2(K+1)))
    
    if (2**k == K+1):
        k -= 1
    
    segs = 2**k
    taken = segs - 1
    
    maxl = ceil((N - taken)/segs)
    minl = floor((N - taken)/segs)
    
    if (maxl == minl):
        flen = maxl
    else:
        q = maxl*segs - (N-taken)
        p = segs - q
        
        assert(p * maxl + q * minl + taken == N)
        
        if (K - taken > p):
            flen = minl
        else:
            flen = maxl
            
    min_lsrs = (flen - 1) // 2
    max_lsrs = flen - min_lsrs - 1
    results.append('%d %d' % (max_lsrs, min_lsrs))


# In[18]:

dout = r'p3\out.txt'

with open(dout, 'w') as f:
    for i, res in enumerate(results):
        f.write("Case #%d: %s\n" % (i+1, str(res)))


# In[17]:

results


# In[ ]:



