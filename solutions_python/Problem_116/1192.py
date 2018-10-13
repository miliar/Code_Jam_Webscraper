def is_won(inp, ch):
    is_empty = False
    for i in xrange(4):
        cnt1, cnt2 = 0, 0
        for j in xrange(4):
            if inp[i][j] in (ch, 'T'):
                cnt1 += 1
            if inp[j][i] in (ch, 'T'):
                cnt2 += 1
            if inp[i][j] == '.':
                is_empty = True               
        if cnt1 == 4 or cnt2 == 4:
             return (True, is_empty)

    cnt1, cnt2 = 0,0
    for i in xrange(4):
        if inp[i][i] in (ch, 'T'):
            cnt1 += 1
        if inp[3-i][i] in (ch, 'T'):
            cnt2 += 1
    if cnt1 == 4 or cnt2 == 4:
        return (True, is_empty)
    return (False, is_empty)            

t = int(raw_input())
for i in xrange(t):
    lns = [ raw_input() for _ in xrange(5) ]
    #print lns
    x_won, is_empty = is_won(lns, 'X')
    if x_won:
         res = "X won"
    else:
        o_won, is_empty = is_won(lns, 'O')
        if o_won:
            res = "O won"
        elif is_empty:
            res = "Game has not completed"
        else:
            res = "Draw"
    print "Case #%s: %s" % (i+1, res)
    
        
