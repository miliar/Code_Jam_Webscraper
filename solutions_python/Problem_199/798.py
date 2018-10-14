import sys

t = int(sys.stdin.readline().strip())
for ti in xrange(t):
    line = sys.stdin.readline().split()
    s = list(line[0])
    k = int(line[1])
    sn = len(s)

    r = 0
    impossible = False
    for i in xrange(sn):
        if s[i] == '-':
            r += 1
            for j in xrange(k):
                if i + j >= sn:
                    impossible = True
                    break
                if s[i + j] == '-':
                    s[i + j] = '+'
                else:
                    s[i + j] = '-'
        if impossible:
            break

    case = "Case #%d: " % (ti + 1)
    if impossible:
        print case + 'IMPOSSIBLE'
    else:
        print case + str(r)

