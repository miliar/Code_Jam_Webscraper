def solve():
    a1 = int(raw_input()) - 1
    m1 = [ map(int, raw_input().split()) for i in xrange(1, 5) ]
    a2 = int(raw_input()) - 1
    m2 = [ map(int, raw_input().split()) for i in xrange(1, 5) ]
    
    common = set(m1[a1]).intersection(set(m2[a2]))
    if len(common) == 1:
        return common.pop()
    if len(common) == 0:
        return 'Volunteer cheated!'
    if len(common) > 1:
        return 'Bad magician!'
    assert False

T = int(raw_input())
for t in xrange(1, T + 1):
    print 'Case #%d: %s' % (t, solve())
