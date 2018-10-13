from Queue import PriorityQueue

t = int(raw_input())  # read a line with a single integer
for x in xrange(1, t + 1):
    N,K = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

    pq = PriorityQueue()
    pq.put((-1*long(N),0))
    
    for i in range(0,K-1):
        #print "Person:", i
        gap_tuple = pq.get()
        gap = -1*gap_tuple[0]
        start = gap_tuple[1]
        #print type(gap)
        #print "Gap:", gap, "Starting after:", start
        g1 = (-1*((gap-1)/2), start)
        g2 = (-1*(gap-1-((gap-1)/2)), start+((gap-1)/2)+1)
        pq.put(g1)
        pq.put(g2)
        #if (g1[0]!=0) :
        #if (g2[0]!=0) :
    
    fg = pq.get()
    gap = -1*fg[0]
    a = (gap-1)/2
    b = (gap-1-((gap-1)/2))
    print "Case #{}: {} {}".format(x, max(a,b), min(a,b))
    #print max(a,b), min(a,b)
