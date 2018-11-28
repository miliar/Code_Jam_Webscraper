T = int(raw_input())
for case in xrange(1,T+1):
    N = int(raw_input())
    wires = [-1] * 10005
    for i in xrange(N):
        wire = map(int,raw_input().split())
        wires[wire[0]] = wire[1]

    intersections = 0
    
    for i in xrange(len(wires)-1):
        if (wires[i] == -1):
            continue
        for j in xrange(i+1,len(wires)):
            if wires[j] == -1:
                continue
            if wires[i] > wires[j]:
                intersections += 1
    print "Case #%d: %d" % (case,intersections)

