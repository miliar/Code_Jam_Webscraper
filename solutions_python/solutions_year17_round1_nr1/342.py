import sys

for cases in xrange( int (sys.stdin.readline() ) ):
    R, C = map( int, sys.stdin.readline().split() )
    print "Case #%d:"%(cases+1)
    ch = '?'
    fillIndex = -1
    cake = []
    for r in xrange( R ):
        row = list(sys.stdin.readline().strip())
        cake.append( row )
        if row.count('?') == C: continue
        c = 0
        ch = ''
        for i in xrange( C ):
            if row[i] == '?':
                if ch == '':
                    c += 1
                else:
                    cake[r][i] = ch
                    c = 0
            else:
                fillIndex = r
                ch = row[i]
                index = i-1
                #print index,c
                while c > 0:
                    cake[r][index] = ch
                    c -= 1
                    index -= 1
        #print cake[r]
    #print fillIndex
    for i in xrange( fillIndex + 1, R ):
        if cake[i].count('?') == C:
             cake[i] = cake[i-1]
        else:
            for j in xrange( C ):
                if cake[i][j] == '?':
                    cake[i][j] = cake[i-1][j]

    for i in xrange( fillIndex-1, -1, -1 ):
        if cake[i].count('?') == C:
             cake[i] = cake[i+1]
        else:
            for j in xrange( C ):
                if cake[i][j] == '?':
                    cake[i][j] = cake[i+1][j]

    for i in cake:  print ''.join(i)
            

                        
        
        
