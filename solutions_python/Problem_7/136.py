N = int(raw_input())
ni = 0
while ni < N:
    line = raw_input()
    n, A, B, C, D, x0, y0, M = ( int(x) for x in line.split() )
    
    T = []
    T.append( (x0, y0) )
    X = x0
    Y = y0
    #print X, Y
    i = 1
    while i < n:
        X = (A * X + B) % M
        Y = (C * Y + D) % M
    #    print X, Y
        T.append( (X, Y) )
        i += 1

    #print T
    i = j = k = counter = 0
    while i < len(T):
        j = i + 1
        while j < len(T):
            k = j + 1
            while k < len(T):
                #print 'x = %d %d %d' % (T[i][0] , T[j][0] , T[k][0], (T[i][0] + T[j][0] + T[k][0]) % 3)
                #print 'y = %d %d %d' % (T[i][1] , T[j][1] , T[k][1], (T[i][1] + T[j][1] + T[k][1]) % 3)
                if (T[i][0] + T[j][0] + T[k][0]) % 3 == 0 and (T[i][1] + T[j][1] + T[k][1]) % 3 == 0:  
                    counter += 1
                k += 1
            j += 1
        i += 1
    
    print 'Case #%d: %d' % (ni+1, counter)
    ni += 1
