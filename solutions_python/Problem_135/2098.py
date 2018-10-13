import sys

n = int(sys.stdin.readline())

for i in range(n):
    s = set(range(1,17))
    for j in range(2):
        r = int(sys.stdin.readline()) - 1
        for j in range(4):
            if j == r:
                t = set([int(x) for x in sys.stdin.readline().split(' ')])
                s = s.intersection(t)
            else:
                sys.stdin.readline()
    if len(s) == 1:
        out = s.pop()
    elif len(s) > 1:
        out = 'Bad magician!'
    else:
        out = 'Volunteer cheated!'
    print 'Case #%d: %s' % (i + 1, out)
