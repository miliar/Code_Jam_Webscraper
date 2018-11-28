f = open('input.txt', 'r')

T = int(f.readline())

for ttt in xrange(1, T + 1):

    R, C = map(int, f.readline().strip().split())

    M = []

    for i in xrange(R):
        M.append(f.readline().strip())

    impos = False

    for i in xrange(R):
        for j in xrange(C):
            if M[i][j] == '#':
                if i == R - 1 or j == C - 1:
                    impos = True
                    break
                if M[i][j + 1] == '#' and M[i + 1][j] == '#' and M[i + 1][j + 1] == '#':
                    M[i] = M[i][:j] + '/\\' + M[i][j + 2:]
                    M[i + 1] = M[i + 1][:j] + '\\/' + M[i + 1][j + 2:]
                else:
                    impos = True
                    break
        if impos:
            break

    print 'Case #{}:'.format(ttt)

    if impos:
        print 'Impossible'
    else:
        for x in M:
            print x
