def check(tup, line):
    #print tup, line, [c in tup for c in line]
    return all([c in tup for c in line])

def sweep(lines):
    for line in lines:
        if check(('O', 'T'), line):
            #print lines
            return True, 'O'
        if check(('X', 'T'), line):
            #print lines
            return True, 'X'

    return False, None

def judge(b):
    res, winner = sweep([[b[i][i] for i in xrange(4)]])
    if res:
        return '{0} won'.format(winner)
    res, winner = sweep([[b[3-i][i] for i in xrange(4)]])
    if res:
        return '{0} won'.format(winner)
    res, winner = sweep(b)
    if res:
        return '{0} won'.format(winner)
    res, winner = sweep(zip(*b))
    if res:
        return '{0} won'.format(winner)


    for row in b:
        for c in row:
            if c == '.':
                return 'Game has not completed'

    return 'Draw'

t = int(raw_input())
for i in xrange(t):
    b = []
    for j in xrange(4):
        b.append(raw_input())

    #print b
    if i < t -1:
        _ = raw_input()
    print "Case #{0}: {1}".format(i + 1, judge(b))
