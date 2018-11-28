f = open('d:/jam/al.in')
fw = open('d:/jam/al.out', 'w')

T = int(f.next())


for i in range(T):
    N = int (f.next())

    As = []
    Bs = []


    for ii in range(N):
        a,b = [int(x) for x in f.next().split(' ')]
        As.append(a)
        Bs.append(b)

    
    secs = 0

    for ii in range(N):
        for jj in range(N):
            if As[ii]>As[jj] and Bs[ii]<Bs[jj]:
                secs += 1

    print 'Case #%d: %d' % (i+1, secs)
    fw.write('Case #%d: %d\n' % (i+1, secs))
                

fw.close()
