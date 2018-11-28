import sys
sin = sys.stdin
T = int(sin.readline().strip())
for i in xrange(1, T+1):
    N, R, O, Y, G, B, V = map(int, sin.readline().strip().split())
    colors = [['R', R, R], ['Y', Y, Y], ['B', B, B]]
    idx = {'R': 0, 'Y': 1, 'B': 2}
    #print 'Input colors: {0}'.format(colors)
    prev = None
    out = []
    for j in xrange(N):
        sel = [x for x in colors if x[0] != prev]
        #print 'selected colors {0}'.format(sel)
        mc = sorted(sel, key=lambda x:-1*x[1]*23)[0]
        #print 'min color {0}'.format(mc)
        color = mc[0]
        prev = color
        colors[idx[color]][1] -= 1
        if colors[idx[color]][1] < 0:
            out = []
            break
        out.append(color)
    if out and out[0] != out[N-1]:
        print 'Case #{0}: {1}'.format(i, ''.join(out))
    else:
        #print 'N-1: {0}, N-3: {1}'.format(N-1, N-3)
        if len(out) == N and out[N-1] != out[N-3]:
            out[N-1] = out[N-2]
            out[N-2] = out[0]
            print 'Case #{0}: {1}'.format(i, ''.join(out))
        else:
            print 'Case #{0}: IMPOSSIBLE'.format(i)
