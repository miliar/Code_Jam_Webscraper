from math import log

def bath(n,m):    
    k = int(log(m,2))
    cand = (n-(2**k-1))/(2**k)
    num = (n-(2**k-1)) % (2**k)
    comp = m-(2**k-1)
    if (comp <= num):
        return [cand-(cand)/2,(cand)/2]
    else:
        return  [cand-(cand-1)/2-1,(cand-1)/2]

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}: {} {}".format(i, bath(n,m)[0], bath(n,m)[1])


