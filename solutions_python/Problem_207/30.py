import sys

IMP = "IMPOSSIBLE"

def compute(N, R, O, Y, G, B, V):
    R0, O0, Y0, G0, B0, V0 = R, O, Y, G, B, V
    r = R - G
    y = Y - V
    b = B - O

    if r == 0 and Y + B + V + O == 0:
        return "GR" * (N / 2)
    if y == 0 and R + G + B + O == 0:
        return "YV" * (N / 2)
    if b == 0 and R + G + Y + V == 0:
        return "BO" * (N / 2)
    if r <= 0 and G > 0:
        return IMP
    if y <= 0 and V > 0:
        return IMP
    if b <= 0 and O > 0:
        return IMP

    c = sorted([[r, 'R'], [y, 'Y'], [b, 'B']])
    n0 = r + y + b
    x = [None] * n0
    if c[2][0] * 2 > n0:
        return IMP
    for i in xrange(c[2][0]):
        x[i * 2] = c[2][1]
    j = 1
    for i in xrange(n0 - 1, -1 ,-1):
        if x[i] is not None:
            continue
        if c[j][0] == 0:
            j = 1 - j
        x[i] = c[j][1]
        c[j][0] -= 1
        j = 1 - j

    y = ""
    for i in xrange(n0):
        y += x[i]
        if x[i] == 'R' and G > 0:
            y += "GR" * G
            G = 0
        if x[i] == 'Y' and V > 0:
            y += "VY" * V
            V = 0
        if x[i] == 'B' and O > 0:
            y += "OB" * O
            O = 0

    if y[0] == y[-1]:
        return IMP
    for i in xrange(1, len(y)):
        if y[i] == y[i-1]:
            return IMP
    R, O, Y, G, B, V = 0, 0, 0, 0, 0, 0
    for q in y:
        if q == 'R':
            R += 1
        elif q == 'O':
            O += 1
        elif q == 'Y':
            Y += 1
        elif q == 'G':
            G += 1
        elif q == 'B':
            B += 1
        elif q == 'V':
            V += 1
    if (R0, O0, Y0, G0, B0, V0) != (R, O ,Y, G, B, V):
        print "ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
    return y

def parse():
    N, R, O, Y, G, B, V = map(int, sys.stdin.readline().strip().split())
    return N, R, O, Y, G, B, V


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        data = parse()
        result = compute(*data)
        print "Case #%d: %s" % (i + 1, result)
