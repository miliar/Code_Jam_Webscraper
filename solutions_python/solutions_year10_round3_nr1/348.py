import sys
import psyco
psyco.full()

cases = int(sys.stdin.readline().strip())
for case in xrange(1, cases + 1):
    n = int(sys.stdin.readline().strip())
    wires = []
    for i in xrange(n):
        wires.append(tuple(map(int, sys.stdin.readline().strip().split(' '))))
    wires.sort()
    c = 0
    for i in xrange(0, len(wires) - 1):
        t = 0
        wi = wires[i]
        for j in xrange(i + 1, len(wires)):
            wj = wires[j]
            da = wj[0] - wi[0]
            db = wj[1] - wi[1]
            if da + db != 0 and wj[1] < wi[1]:
                c += 1
    print 'Case #%d: %d' % (case, c)
