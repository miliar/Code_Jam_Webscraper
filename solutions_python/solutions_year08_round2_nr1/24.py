ifile = file('A-large.in')
#ifile = file('test.in')
#ifile = file('A-small.in')
#ifile = file('A-large.in')

num = int(ifile.readline())

for kk in xrange(num):
    n, A, B, C, D, x0, y0, M = map(int,ifile.readline().strip().split(' '))
    X = x0; Y = y0
    points = {}
    
    try:    points[(X % 3, Y % 3)] += 1
    except: points[(X % 3, Y % 3)] = 1
#    print X,Y
    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
#        print X,Y
        try:    points[(X % 3, Y % 3)] += 1
        except: points[(X % 3, Y % 3)] = 1

#    print points
    total = 0
    count = []
#    print points
    for i in points:
        for j in points:
#            if j < i: continue
            for k in points:
                if set([i,j,k]) in count: continue
                else: count.append(set([i,j,k]))
                if (i[0] + j[0] + k[0]) % 3 == 0 and (i[1]+j[1]+k[1]) % 3 == 0:
#                    print i,j,k
                    if i == j and j == k:
                        total += points[i] * (points[i] -1) * (points[i] -2) / 6
#                    elif i == j and j != k:
#                        print 'a'
#                        total += points[i] * (points[i] -1) * points[k] / 2
#                    elif j == k and i != j:
#                        print 'b'
#                        total += points[i] * (points[k] -1) * (points[k]) / 2
                    elif i != j and j != k and i != k:
                        total += points[i] * points[j] * points[k]
                    else:
                        print 'error'
                
    print "Case #%s: %s"%(kk+1,total)