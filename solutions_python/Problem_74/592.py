cases = raw_input()
for case in xrange(int(cases)):
    q = raw_input().strip().split()
    buttons = int(q.pop(0))
    p = 0
    times = 0
    
    b = 0
    o = 0
    poso = 1
    posb = 1
    wait = ''
    justpush = False
    
    while p < buttons:
        if wait == '':
            try:
                oi = q.index('O')
            except:
                oi = None
            try:
                bi = q.index('B')
            except:
                bi = None

            if oi == None:
                wait = 'B'
            elif bi == None:
                wait = 'O'
            elif oi < bi:
                wait = 'O'
            else:
                wait = 'B'
        
        if o == 0:
            if oi != None:
                oi = q.index('O')
                o = int(q[oi+1])
        if b == 0:
            if bi != None:
                bi = q.index('B')
                b = int(q[bi+1])
        
        if wait == 'O':
            if poso == o:
                p += 1
                wait = ''
                o = 0
                q.pop(oi)
                q.pop(oi)
            else:
                if poso < o:
                    poso += 1
                elif poso > o:
                    poso -= 1
            if posb < b:
                posb += 1
            elif posb > b:
                posb -= 1
            times += 1

        elif wait == 'B':
            if posb == b:
                p += 1
                wait = ''
                b = 0
                q.pop(bi)
                q.pop(bi)
            else:
                if posb < b:
                    posb += 1
                elif posb > b:
                    posb -= 1
            if poso < o:
                poso += 1
            elif poso > o:
                poso -= 1
            times += 1

    print 'Case #%d: %d' % (case + 1, times)
