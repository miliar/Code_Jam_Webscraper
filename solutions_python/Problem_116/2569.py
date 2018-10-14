import sys


def getWin(a):
    xc = a.count('X')
    oc = a.count('O')
    t = (a.count('T') == 1)
    winner = None
    if xc == 4 or (xc == 3 and t):
        winner = 'X'
    elif oc == 4 or (oc == 3 and t):
        winner = 'O'
    dots = a.count('.')
    return winner, dots > 0


T = int(sys.stdin.readline().strip())
t = 0
while t < T:
    t += 1 
    #read board, read diags while doing it
    diag1 = [''] * 4
    diag2 = [''] * 4
    l1 = list(sys.stdin.readline().strip())
    #print l1
    diag1[0] = l1[0]
    diag2[3] = l1[3]
    l2 = list(sys.stdin.readline().strip())
    #print l2
    diag1[1] = l2[1]
    diag2[2] = l2[2]
    l3 = list(sys.stdin.readline().strip())
    #print l3
    diag1[2] = l3[2]
    diag2[1] = l3[1]
    l4 = list(sys.stdin.readline().strip())
    #print l4
    diag1[3] = l4[3]
    diag2[0] = l4[0]
    #print diag1
    #print diag2
    sys.stdin.readline()

    #count entries in arrays
    draw = True
    allq = [l1, l2, l3, l4]

    #diags
    res, dots = getWin(diag1)
    if dots: draw = False
    if res:
        print 'Case #%d: %s won' % (t, res)
        continue

    res, dots = getWin(diag2)
    if dots: draw = False
    if res:
        print 'Case #%d: %s won' % (t, res)
        continue
    
    #hori
    for a in allq:
        res, dots = getWin(a)
        if dots: draw = False
        if res:
            print 'Case #%d: %s won' % (t, res)
            break
    if res: continue

    #vert
    allv = [ [e[0] for e in allq], 
             [e[1] for e in allq],
             [e[2] for e in allq],
             [e[3] for e in allq],
            ]
    
    for a in allv:
        res, dots = getWin(a)
        if dots: draw = False
        if res:
            print 'Case #%d: %s won' % (t, res)
            break
    if res: continue
    
    #on winner continue loop
    if draw:
        print 'Case #%d: Draw' % (t,)
    else:
        print 'Case #%d: Game has not completed' % (t,)
        
