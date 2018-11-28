from bisect import bisect_left
import time
import sys

start = time.time()
list = [1,2,3]

# 202
for i in range(49):
    list.append(int('2%s2' % ''.join('0' for j in range(i))))
    
# 212
for i in range(25):
    x = ''.join('0' for j in range(i))
    list.append(int('2%s1%s2' % (x,x)))
    
# 121
for i in range(25):
    x = ''.join('0' for j in range(i))
    list.append(int('1%s2%s1' % (x,x)))

# 11211
for i in range(24):
    x = ''.join('0' for j in range(i))
    for j in range(24-i):
        y = ''.join('0' for k in range(j))
        list.append(int('1%s1%s2%s1%s1' % (y,x,x,y)))

p = [10**i for i in range(50)]
        
def go(n, k, x, list):
    if k == 0:
        xi = str(x)[::-1]
        list.append(int('%s%s' % (x,xi)))
        list.append(int('%s0%s' % (x,xi)))
        list.append(int('%s1%s' % (x,xi)))
    if n == 0:
        return
    for i in xrange(n):
        go(i, k-1, p[i] + x, list)
    
for k in [1,2,3,4]:
    go(25, k, 0, list)
           
list = [x*x for x in list]
list.sort()
#for x in list: print x
#print len(list)

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] >= x else -1) # don't walk off the end

#print time.time() - start

import sys

cas = int(sys.stdin.readline()[:-1])
for z in range(cas):
    s = sys.stdin.readline()
    if s[-1] == '\n':
        s = s[:-1]
    a, b = (int(x) for x in s.split(' '))
    aa = binary_search(list, a)
    bb = binary_search(list, b)
    if list[bb] == b:
        bb += 1
    print 'Case #%d: %d' % (z+1, bb-aa)


