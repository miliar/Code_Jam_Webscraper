T = int(raw_input())
for case in xrange(T):
    numwires = int(raw_input())
    
    wires = []
    for w in xrange(numwires):
        wires.append(map(int, raw_input().split(" ")))
    
    '''
    intersections = 0
    for w1 in wires:
        for w2 in wires:
            if w1 != w2 and w1[0] < w2[0] and w1[1] > w2[1]:
                intersections += 1
    '''
    
    a_running_sum = [set() for i in xrange(10**4+2)]
    b_running_sum = [set() for i in xrange(10**4+2)]
    for i, (a, b) in enumerate(wires):
        a_running_sum[a].add(i)
        b_running_sum[b].add(i)
    for i in xrange(1, len(a_running_sum)):
        a_running_sum[i].update(a_running_sum[i-1])
        b_running_sum[i].update(b_running_sum[i-1])
    intersections = 0
    for a, b in wires:
         intersections += len((a_running_sum[-1] - a_running_sum[a]) & (b_running_sum[b]))
         intersections += len((a_running_sum[a]) & (b_running_sum[-1] - b_running_sum[b]))
    intersections /= 2
    
    print "Case #%s: %s" %(case+1, intersections)