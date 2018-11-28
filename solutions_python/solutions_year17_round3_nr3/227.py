import math, heapq

t = int(raw_input())

for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]
    u = float(raw_input())
    p = [float(s) for s in raw_input().split(" ")]
    
    p.sort();
    
    for j in xrange(n):
        avg = (sum(p[:j+1]) + u) / (j + 1)
        if j == n - 1:
            break
        if avg < p[j + 1]:
            break
    
    avg = min(1, avg)
    for k in xrange(j+1):
        p[k] = avg
    
    ans = 1;
    for j in xrange(n):
        ans = ans * p[j]

    print "Case #{}: {:0.7f}".format(i, ans)
