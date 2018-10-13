def read_answer():
    arow = int(raw_input())
    for i in xrange(4):
        row = raw_input()
        if arow == (i+1):
            answer = set(row.split())
    return answer

T = int(raw_input())
for t in xrange(T):
    one = read_answer()
    two = read_answer()
    common = one.intersection(two)
    if len(common) == 1:
        print 'Case #{}: {}'.format(t+1, common.pop())
    elif len(common) < 1:
        print 'Case #{}: Volunteer cheated!'.format(t+1)
    else:
        print 'Case #{}: Bad magician!'.format(t+1)
