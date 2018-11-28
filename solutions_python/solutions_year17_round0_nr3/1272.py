from heapq import heappush as hpush, heappop as hpop


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N, K = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case


    
    h = []
    hpush(h, (-N, N))
    for _ in xrange(K-1):
        # print h
        _, a = hpop(h)
        # print a, 
        if a > 1:
            hpush(h, (-(a/2), a/2))
        if a > 2:
            hpush(h, (-((a-1)/2), (a-1)/2))
     
    _, a = hpop(h)
    # print a
     
    p, q = a / 2, (a-1) / 2





    print "Case #{}: {} {}".format(i, p, q)

