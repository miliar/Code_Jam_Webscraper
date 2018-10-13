def B():
    #===Reading File========================================
    f = open('B-small-attempt0.in')
    T = int(f.readline())
    #=======================================================


    for t in xrange(T):
        N, M = f.readline().split()
        N, M = int(N), int(M)
        field = {}
        minimum = 100
        isDone = False
        for x in xrange(N):
            line = [int(m) for m in f.readline().split()]
            if minimum > min(line):  minimum = min(line)
            for y in xrange(M):
                field[(x,y)] = line[y]
                
        for item in field:
            if field[item] == minimum:
                #print item[0], item[1]
                for m in xrange(M):
                    if field[item[0], m] > minimum:
                        for n in xrange(N):
                            if field[n, item[1]] > minimum:
                                print 'Case #'+str(t+1)+': NO'
                                isDone = True
                                break
                        if isDone == True: break
            if isDone == True: break
        if isDone == False:
            print 'Case #'+str(t+1)+': YES'

