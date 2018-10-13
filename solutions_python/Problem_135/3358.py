import sys

t = int(sys.stdin.readline())

for z in range(t):
    a = int(sys.stdin.readline()) - 1
    q = [[]] * 4

    for i in range(4):
        q[i] = [int(x) for x in sys.stdin.readline().split()]


    b = int(sys.stdin.readline()) - 1
    w = [[]] * 4

    for i in range(4):
        w[i] = [int(x) for x in sys.stdin.readline().split()]

    r = [x for x in q[a] if x in w[b]]
    print 'Case #{0}: {1}'.format(z + 1, 'Volunteer cheated!' if len(r) == 0 else r[0] if len(r) == 1 else 'Bad magician!')
