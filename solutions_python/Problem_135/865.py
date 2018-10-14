from sys import stdin

T = int(stdin.readline())

for k in xrange(T):
    pos = [[0, 0] for j in xrange(16)]
    diff = [[[] for l in xrange(4)] for j in xrange(4)]

    a1 = int(stdin.readline())-1
    p1 = [map(int, stdin.readline().split()) for j in xrange(4)]

    a2 = int(stdin.readline())-1
    p2 = [map(int, stdin.readline().split()) for j in xrange(4)]

    for i in xrange(4):
        for j in xrange(4):
            pos[p1[i][j] - 1][0] = i
            pos[p2[i][j] - 1][1] = i

    for i, (a, b) in zip(xrange(16), pos):
        diff[a][b].append(i)

    c = len(diff[a1][a2])

    print 'Case #%d:' % (k+1),

    if c == 1:
        print diff[a1][a2][0]+1
    elif c > 1:
        print 'Bad magician!'
    else:
        print 'Volunteer cheated!'
