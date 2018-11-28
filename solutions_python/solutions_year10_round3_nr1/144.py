import sys

T = int(sys.stdin.readline())

def solve(wires):
    intersections = 0
    for i, (al, ar) in enumerate(wires):
        for j in range(i+1, len(wires)):
            bl, br = wires[j]
            if (al < bl and ar > br) or (al > bl and ar < br):
                intersections += 1
    return intersections
        

for i in range(T):
    # i = int(sys.stdin.readline())
    # s = sys.stdin.readline().strip('\n')
    # l = sys.stdin.readline().strip('\n').split()
    N = int(sys.stdin.readline())
    wires = []
    for j in range(N):
        A, B = sys.stdin.readline().split()
        wires.append((int(A), int(B)))
    print 'Case #%s: %s' % (i+1, solve(wires))
