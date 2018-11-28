import numpy as np
t = int(raw_input())
for i in xrange(1,t+1):
    n, k = raw_input().split(" ")
    n = int(n)
    k = int(k)
    if k == 1:
        print ("Case #{}: {} {}".format(i, n/2, (n/2) if not n % 2 == 0 else (n/2-1)))
    elif n == k:
        print ("Case #{}: {} {}".format(i, 0, 0))
    else:
        l = []
        l.append(n/2)
        l.append(n/2) if not n % 2 == 0 else l.append(n/2-1)
        for x in xrange(1,k):
            ind = np.argmax(l)
            max = l.pop(ind)
            l.append(max/2)
            l.append(max/ 2) if not max % 2 == 0 else l.append(max/2-1)
        print("Case #{}: {} {}".format(i, max/2, max/2 if not max % 2 == 0 else max/2-1))
