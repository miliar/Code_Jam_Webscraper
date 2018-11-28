import sys

t = int(sys.stdin.readline())
for c in range(1, t + 1):
    s1 = set()
    s2 = set()
    r1 = int(sys.stdin.readline())
    for i in range(1, 5):
        f = sys.stdin.readline().strip().split()
        if i == r1:
            s1 = set(f)
    r2 = int(sys.stdin.readline())
    for i in range(1, 5):
        f = sys.stdin.readline().strip().split()
        if i == r2:
            s2 = set(f)

    inter = s1.intersection(s2)
    if len(inter) == 1:
        print 'Case #%d: %s' %(c, list(inter)[0])
    elif len(inter) > 1:
        print 'Case #%d: Bad magician!' %c
    else:
        print 'Case #%d: Volunteer cheated!' %c

