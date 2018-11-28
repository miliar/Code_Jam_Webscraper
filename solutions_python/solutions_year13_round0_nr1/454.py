T = int(raw_input())


dig = [ [(0, 0), (1, 1), (2, 2), (3, 3)], [(0, 3), (1, 2), (2, 1), (3, 0)]]

for z in xrange(T):
    rary = [ raw_input() for i in xrange(4) ]
    raw_input()

    cary = [ ''.join([ rary[i][j] for i in xrange(4) ]) for j in xrange(4) ]

    dary = [ ''.join([ rary[r][c] for r, c in lst ]) for lst in dig ]

    ary = rary + cary + dary

    #print ary
    X = any(s.count('X') == 4 or (s.count('X') == 3 and s.count('T') == 1) for s in ary )
    O = any(s.count('O') == 4 or (s.count('O') == 3 and s.count('T') == 1) for s in ary )
    ct = sum( s.count('.') for s in rary )

    if X:
        ans = 'X won'
    elif O:
        ans = 'O won'
    elif ct == 0:
        ans = 'Draw'
    else:
        ans = 'Game has not completed'

    print 'Case #%d: %s' % (z+1, ans)

