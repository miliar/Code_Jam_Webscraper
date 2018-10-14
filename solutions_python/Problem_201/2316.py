import math
from Queue import PriorityQueue
t = int(raw_input().strip())

for a in xrange(t):
    n, k = [int(x) for x in raw_input().strip().split()]
    q = PriorityQueue()
    q.put((-n, n))
    for i in range(k):
        gap = q.get()[1] - 1
        small = gap // 2
        large = int(math.ceil(float(gap)/2))
        if small == 0 and large == 0:
            break
        q.put((-small, small))
        q.put((-large, large))

    print "Case #{}: {} {}".format(a+1, large, small)