import sys
import math
import operator

def solve_simple(N, U, Ps):
    Ps = Ps + [1.0]
    ps = sorted(Ps)

    #print ps

    Incr = None
    while U > 0:
        mingroup = [ps[0]]
        for p in ps[1:]:
            if p == mingroup[0]:
                mingroup.append(p)
            else:
                Diff = p - mingroup[0]
                C = len(mingroup)
                if Diff * C <= U:
                    Each = Diff
                else:
                    Each = U / C
                #print 'Will add', Each, 'to', C
                break
        for i in xrange(C):
            ps[i] += Each
        U -= Each*C
        #print 'U is', U
        #print 'PS', ps

    ret = reduce(operator.__mul__, ps, 1.0)
    #print 'got', ret
    return min(ret, 1)

def solve(N, K, U, Ps):

    if N == K:
        return solve_simple(N, U, Ps)

    return 'DK'

def main():
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        N, K = map(int, sys.stdin.readline().split())
        U = float(sys.stdin.readline())
        Ps = map(float, sys.stdin.readline().split())
        ans = solve(N, K, U, Ps)
        print 'Case #%s: %s' % (i+1, ans)

if __name__ == '__main__':
    main()
