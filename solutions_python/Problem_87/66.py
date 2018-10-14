from sys import stdin
buf = [(l).strip() for l in stdin]
buf.reverse()

def solve():
    X, wS, rS, T, N = tuple(int(e) for e in buf.pop().split())
    ww = [tuple(float(e) for e in buf.pop().split()) for i in range(N)]
    # BEW
    I = [(w, y-x) for x, y, w in ww]
    I.append((0.0, X - sum(l for w, l in I)))
    I.sort()
    time = 0.0
    running = True
    for w, l in I:
#        print 'w =', w, ' ; l =', l
#        print ['walking', 'running'][running]
        if running:
            dt = l/(w+rS)
            if dt <= T:
                time += dt
#                print dt
                T -= dt
                continue
            time += T
#            print T
            l -= (w+rS) * T
#            print 'stopped running'
            running = False
        time += l/(w+wS)
#        print l/(w+wS)
    return time

T = int(buf.pop())
for i in range(T):
    print 'Case #%d:' % (i+1), solve()
