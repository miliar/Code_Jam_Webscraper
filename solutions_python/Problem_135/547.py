def grid():
    g = []
    for i in range(4):
        g.append(set(int(x) for x in raw_input().split()))
    return g

def case():
    ans1 = int(raw_input())
    g = grid()

    ans2 = int(raw_input())
    h = grid()
    
    i = g[ans1-1] & h[ans2-1]

    if len(i) == 1:
        return str(i.pop())
    if len(i) == 0:
        return 'Volunteer cheated!'
    return 'Bad magician!'

cases = int(raw_input())
for i in xrange(cases):
    print 'Case #%d: %s' % (i+1, case())


