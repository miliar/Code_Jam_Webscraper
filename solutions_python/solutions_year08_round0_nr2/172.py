ifile = file('B-small-attempt3.in')

num = int(ifile.readline())

for kk in xrange(num):
    
    m = int(ifile.readline())
    
    a, b = map(int, ifile.readline().split(' '))
    scha = []
    for aa in xrange(a):
        scha.append(map(lambda i: int(i[:2]) * 60 + int(i[3:]), ifile.readline().split(' ')))
        
    schb = []
    for bb in xrange(b):
        schb.append(map(lambda i: int(i[:2]) * 60 + int(i[3:]), ifile.readline().split(' ')))
    
#    if kk != 14: continue
#    print a,b
    
    
    scha.sort(key = lambda i: i[0])
    schb.sort(key = lambda i: i[1])
    
    queuea = list(scha)
    queueb = list(schb)
    
    t = 0
    for i in scha:
        if queueb and queueb[0][1] + m <= i[0]:
            t+= 1
            queueb.pop(0)            
        
#    print 'a', len(scha) - t
    ta = len(scha) - t
    
    scha.sort(key = lambda i: i[1])
    schb.sort(key = lambda i: i[0])
    
    queuea = list(scha)
    queueb = list(schb)
    
    
    t = 0
    for i in schb:
        if queuea and queuea[0][1] + m <= i[0]:
            t += 1
            queuea.pop(0)
        
#    print 'b', len(schb) - t
    tb = len(schb) - t
    
        
    print 'Case #%s: %s %s'%(kk + 1, ta, tb)
                