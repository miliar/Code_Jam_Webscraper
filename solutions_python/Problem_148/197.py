import sys

lines = [map(int, line.strip().split(' ')) for line in sys.stdin.readlines()]
T = lines[0][0]

line = 1
for t in range(T):
    N, X = lines[line]
    elements = sorted(lines[line + 1])
    line += 2

    mx = len(elements) - 1
    mn = 0

    s = 0
    while mx >= mn:
        if mx == mn:
            # print mx
            mx -= 1
        elif elements[mx] + elements[mn] > X:
            # print mx
            mx -= 1
        else:
            # print mx, mn
            mx -= 1
            mn += 1
        s += 1


    solution = s
    print "Case #%d: %s" % (t + 1, solution)
