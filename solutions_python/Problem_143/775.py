#!/usr/bin/python
import sys
import time

def count(a, b, k):
    total = 0
    for i in range(0, a):
        for j in range(0, b):
            if (i&j) < k:
			   total += 1
    return total

if __name__ == "__main__":
    start = time.time()
    sys.stderr.write(str(start))
    t = int(raw_input())
    cases = t
    res = []
    while t > 0:
        a, b, k  = raw_input().split(" ")
        a = int(a)
        b = int(b)
        k = int(k)
        res.append(count(a, b, k))
        t = t - 1
    for i in range(1, cases+1):
        print "Case #" + str(i) + ":", str(res[i-1])
    sys.stderr.write('\n')
    sys.stderr.write(str(time.time()-start))
