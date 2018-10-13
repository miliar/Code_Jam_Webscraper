import math
def solve(D, vines):
    vines.append((D, 0)) # treat lover as vine
    vines.sort()
    reach = [-1]*len(vines)
    reach[0] = vines[0][0]
    for i in xrange(len(vines)):
        h = reach[i]
        if h < 0:
            break

        di = vines[i][0]
        for j in xrange(i+1, len(vines)):
            dj, lj = vines[j]
            if dj-di > h:
                break

            hj = min(lj, dj-di)
            reach[j] = max(reach[j], hj)
#        print reach
    return reach[-1] >= 0

T = int(raw_input())
for case in xrange(1, T+1):
    N = int(raw_input())
    vines = [map(int, raw_input().split()) for i in xrange(N)]
    D = int(raw_input())
    print 'Case #%i:' % case,
    if solve(D, vines):
        print 'YES'
    else:
        print 'NO'
