def solve(ropes):
    intersections = set()
    ropes.sort()
    for i in xrange(len(ropes)):
        A, B = ropes[i]
        for j in xrange(len(ropes)):
            if i != j:
                a, b = ropes[j]
                if j < i:
                    if b > B:
                        intersections.add(frozenset([i, j]))
                else:
                    assert j > i
                    if b < B:
                        intersections.add(frozenset([i, j]))
    return len(intersections)

if __name__ == '__main__':
    T = input()
    for x in xrange(T):
        N = input()
        ropes = []
        for _ in xrange(N):
            a, b = (int(x) for x in raw_input().split())
            ropes.append((a, b))
        y = solve(ropes)
        print 'Case #%d: %d' % (x + 1, y)
