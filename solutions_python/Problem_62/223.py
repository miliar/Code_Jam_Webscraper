import sys

def intersect(wire1, wire2):
    return (wire2[0] > wire1[0] and wire2[1] < wire1[1]) or (wire2[0] < wire1[0] and wire2[1] > wire1[1])
    

def solve(wires):
    res = 0
    N = len(wires)

    for i in xrange(N):
        for j in xrange(i + 1, N):
            if intersect(wires[i], wires[j]):
                res += 1

    return res

T = int(raw_input())

for t in xrange(T):
    N = map(int, sys.stdin.readline().split(' '))[0]
    wires = [map(int, sys.stdin.readline().split(' ')) for i in xrange(N)]

    print 'Case #%d: %d' % (t+1, solve(wires))
