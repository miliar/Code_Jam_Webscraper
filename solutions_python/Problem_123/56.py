import sys

# read int
n = int(sys.stdin.readline().strip())

for case in range(n):
    # read many ints
    ns = map(int, filter(lambda x: x != '',
                        map(lambda x: x.strip(),
                                sys.stdin.readline().split(' '))))
    A, N = ns[0], ns[1]
    V = map(int, filter(lambda x: x != '',
                        map(lambda x: x.strip(),
                                sys.stdin.readline().split(' '))))
    V = sorted(V)
    i = 0
    while i < len(V) and A > V[i]:
        A = A + V[i]
        i = i + 1
    bestForNow = len(V) - i
    inserted = 0
    if A > 1:
        while i < len(V):
            while V[i] >= A:
                A = A + A - 1
                inserted = inserted + 1
            A = A + V[i]
            i = i + 1
            bestForNow = min(bestForNow, inserted + (len(V) - i))
        
    print 'Case #%d: %s' % (case + 1, bestForNow)