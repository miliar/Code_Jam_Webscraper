
# coding: utf-8

# In[10]:

def div_up(x, y):
    return x / y + (x % y != 0)

def solve(groups, P):
    buckets = { k : len([g for g in groups if g % P == k]) for k in xrange(P)}
    if P == 2:
        return buckets[0] + div_up(buckets[1],2)
    if P == 3:
        return buckets[0] + min(buckets[1], buckets[2]) +             div_up(max(buckets[1], buckets[2]) - min(buckets[1], buckets[2]), 3)
    assert P == 4
    rv = buckets[0] + min(buckets[1], buckets[3]) + (buckets[1] / 2)
    x = max(buckets[1], buckets[3]) - min(buckets[1], buckets[3])
    y = buckets[1] % 2
    if y == 0:
        return rv + div_up(x, 4)
    else:
        if x >= 2:
            return rv + 1 + div_up(x - 2, 4)
        else:
            return rv + 1
    


# In[11]:

import sys
f = sys.stdin
# f = open("q1_example.in")
T = int(f.readline())
for t in xrange(1, T + 1):
    N, P = map(int, f.readline().split())
    groups = map(int, f.readline().split())
    print "Case #%d: %d" % (t, solve(groups, P))


# In[ ]:



