for case in xrange(input()):
    N = int(raw_input())
    #print "N:", N
    floors = [ ( (0,0), 0 ) for _ in xrange(N) ]
    #print floors
    count = 0
    for line in xrange(N):
        A, B = [int(x) for x in raw_input().split() ]
        #print A, B
        floors[line] = ( (A, B), 0 )
        for i in xrange(line):
            ai, bi = floors[i][0]
            #print ai, bi
            if (A - ai)*(B - bi) < 0:
                count += 1
        #total
    print "Case #%d: %d" % (case+1, count)
        
