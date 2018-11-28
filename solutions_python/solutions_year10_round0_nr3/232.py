T = int(raw_input())

for case in xrange(1,T+1):
    R, K , N = map(int, raw_input().split())
    li = map(int, raw_input().split())
    E = 0
    index = 0
    size  = len(li)
    for r in xrange(R):
        Oc = li[index]
        start = index
        index += 1
        index %= size
        while (Oc + li[index] <= K and index != start ):
            Oc += li[index]
            index += 1
            index %= size
        E += Oc
    print "Case #%d: %d" % (case, E)
    
