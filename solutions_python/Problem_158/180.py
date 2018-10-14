for t in xrange(input()):
    x, r, c = map(int, raw_input().split())
    r, c = min(r, c), max(r, c)
    if x > c: win = True
    elif (x+1)/2 > r: win = True
    elif (r*c)%x != 0: win = True
    elif x == 1: win = False
    elif x == 2: win = (r*c)%2 == 1
    elif x == 3: win = False
    elif x == 4: win = r == 2
    else: win = True
    print 'Case #%d: %s' % (t+1, 'RICHARD' if win else 'GABRIEL')
