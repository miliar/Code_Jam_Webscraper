# Python 2.7

n_cases = int(raw_input())
for ctr in xrange(1, n_cases+1):
    r1 = int(raw_input())
    assert 1 <= r1 <= 4
    rows1 = []
    for _ in xrange(4):
        s = set([int(x) for x in raw_input().split(' ')])
        assert len(s) == 4
        rows1.append(s)
    
    r2 = int(raw_input())
    assert 1 <= r2 <= 4
    rows2 = []
    for _ in xrange(4):
        s = set([int(x) for x in raw_input().split(' ')])
        assert len(s) == 4
        rows2.append(s)


    isec = rows1[r1-1].intersection(rows2[r2-1])
    assert 0 <= len(isec) <= 4
    if len(isec) == 1:
        print('Case #%d: %d' % (ctr, isec.pop()))
    elif len(isec) == 0:
        print('Case #%d: Volunteer cheated!' % ctr)
    else:
        print('Case #%d: Bad magician!' % ctr)
