import sys

t = int(sys.stdin.readline().strip())

for tt in xrange(t):
    n = [int(k) for k in list(sys.stdin.readline().strip())]
    i = 0
    while (i < len(n) - 1):
        if n[i] > n[i + 1]:
            n[i] -= 1
            for j in range(i + 1, len(n)):
                n[j] = 9
            if i > 0:
                i -= 1
        else:
            i += 1

    while (n[0] == 0) and (len(n) > 1):
        n.pop(0)

    print "Case #%d:" % (tt + 1), "".join([str(k) for k in n])

