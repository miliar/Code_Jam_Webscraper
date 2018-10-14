import sys
line = sys.stdin.readline()
numTests = int(line)
for test in xrange(1, numTests+1):
    lawnDim = sys.stdin.readline()
    lawnDim = lawnDim.split(' ')
    N = int(lawnDim[0])
    M = int(lawnDim[1])
    lawn = []
    maxHeight = 0
    for i in xrange(N):
        lawnConfig = sys.stdin.readline()
        lawnConfig = lawnConfig.split(' ')
        lawnConfig = [int(x) for x in lawnConfig]
        lawn.append(lawnConfig)
        maxHeight = max(max(lawnConfig), maxHeight)

    #print maxHeight
    #for i in xrange(N+2):
    #    print lawn[i]

    col_constraints = {}
    row_constraints = {}
    config_fail = False
    for h in xrange(maxHeight, 0, -1):
        #print h
        for i in xrange(0, N):
            for j in xrange(0, M):
                #print lawn[i][j],
               col_fail = False
               row_fail = False
               if (h == lawn[i][j]):
                   if (col_constraints.has_key(i)):
                       if (col_constraints[i] > h):
                           col_fail = True
                   else:
                       col_constraints[i] = h

                   if (row_constraints.has_key(j)):
                       if (row_constraints[j] > h):
                           row_fail = True
                   else:   
                       row_constraints[j] = h

               if (row_fail and col_fail):           
                   config_fail = True

    if (config_fail):
         print 'Case #%d: NO' %(test)
    else:
         print 'Case #%d: YES' %(test)
