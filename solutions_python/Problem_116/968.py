T = int(raw_input())
for t in range(T):
    print "Case #"+str(t+1)+":",
    if t:
        raw_input()
    xs = lambda x: x=='X' or x=='T'
    os = lambda x: x=='O' or x=='T'
    rows = [list(raw_input()) for i in xrange(4)]
    cols = [[rows[j][i] for j in xrange(4)] for i in xrange(4)]
    diags = [[rows[i][i] for i in xrange(4)],[rows[i][4-i-1] for i in xrange(4)]]
    done = False
    for i in rows:
        if all(map(xs,i)):
            print 'X won'
            done = True
            break
        if all(map(os,i)):
            print 'O won'
            done = True
            break
    if done: continue
    for i in cols:
        if all(map(xs,i)):
            print 'X won'
            done = True
            break
        if all(map(os,i)):
            print 'O won'
            done = True
            break
    if done: continue
    for i in diags:
        if all(map(xs,i)):
            print 'X won'
            done = True
            break
        if all(map(os,i)):
            print 'O won'
            done = True
            break
    if done: continue
    for i in rows:
        if '.' in i:
            print 'Game has not completed'
            done = True
            break
    if done: continue
    print 'Draw'
