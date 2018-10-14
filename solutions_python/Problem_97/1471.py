import sys

t = int(sys.stdin.readline())
for i in range(t):
    A, B = map(int, sys.stdin.readline().split())
    count = 0
    for j in range(A, B+1):
        n = str(j)
        m = n
        found = set()
        for k in range(len(m)-1):
            m = m[-1] + m[:-1]
            im = int(m)
            if im <= B and im > j and im not in found:
                count += 1
                found.add(im)
    print "Case #%d: %d" % (i+1, count)
