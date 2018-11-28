
n = int(raw_input())
for i in xrange(n):
    w = raw_input()
    n = int(w.split()[0])
    m = int(w.split()[1])
    
    # c = 0
    # for j in xrange(n+1,m+1):
        # for k in xrange(n,j):
            # if j>k:
                # temp = str(k)
                # for l in xrange(len(temp)-1):
                    # temp = temp[-1] + temp[:len(temp)-1]
                    # if int(temp)==j:
                        # c += 1
                        # if i==3:
                            # print i+1, j,k
    # print 'Case #%d: %d' % (i+1,c)

    c = []
    for j in xrange(n+1,m+1):
        for k in xrange(n,j):
            if j>k:
                temp = str(k)
                for l in xrange(len(temp)-1):
                    temp = temp[-1] + temp[:len(temp)-1]
                    if int(temp)==j and ([j,k] not in c):
                        c.append([j,k])
    print 'Case #%d: %d' % (i+1,len(c))