import sys

T = int(sys.stdin.readline())
for t, line in enumerate(sys.stdin):
    tokens = line.split()
    N = int(tokens[0])
    S = int(tokens[1])
    p = int(tokens[2])
    tp = [int(tok) for tok in tokens[3:]]
    out = 0
    for pts in tp:
        x = pts // 3
        if pts % 3 == 0:
            if x >= p:
                out += 1
            elif x+1 >= p and x-1 >= 0 and S > 0:
                out += 1
                S -= 1
        elif pts % 3 == 1:
            if x+1 >= p:
                out += 1
        else:
            if x+1 >= p:
                out += 1
            elif x+2 >= p and S > 0:
                out += 1
                S -= 1
    print 'Case #%d: %d' % (t+1, out)
