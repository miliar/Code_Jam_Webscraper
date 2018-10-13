import sys
rl = sys.stdin.readline

def solve1(V, X, r0, c0):
    if X == c0:
        return V / r0
    else:
        return 1e30

from sympy.solvers import solve
import sympy

def mix(v0, x0, v1, x1):
    return (v0 * x0 + v1 * x1) / (v0 + v1)

def solve2(V, X, r0, c0, r1, c1):
    t0 = sympy.Symbol('t0')
    t1 = sympy.Symbol('t1')
    r0 = sympy.Float(r0)
    c0 = sympy.Float(c0)
    r1 = sympy.Float(r1)
    c1 = sympy.Float(c1)
    V = sympy.Float(V)
    X = sympy.Float(X)

    ret = solve([
        r0 * t0 + r1 * t1 - V,
        mix(r0 * t0, c0, r1 * t1, c1) - X
    ])
#    sys.stderr.write("%s\n" % str(ret))
#    sys.stderr.flush()
    if not ret:
        return 1e30
    elif not t1 in ret:
        ret = solve([
            (ret[t0] - t1)
        ])
        #print ret
        t1_v = t0_v = ret[t1]
        sys.stderr.write("%s\n" % t1_v); sys.stderr.flush()
    else:
        t0_v = (ret[t0])
        t1_v = (ret[t1])
    if t0_v < 0 or t1_v < 0: return 1e30
#    print t0_v, t1_v
    return max(t0_v, t1_v)

def main():
    T = int(rl())
    for kase in range(1, T+1):
        N, V, X = map(float, rl().split())
        N = int(N + 1e-9)
        if N == 1:
            r0, c0 = map(float, rl().split())
            ans = solve1(V, X, r0, c0)
        else:
            r0, c0 = map(float, rl().split())
            r1, c1 = map(float, rl().split())
            ans = solve2(V, X, r0, c0, r1, c1)
            ans = min(ans, solve1(V, X, r0, c0))
            ans = min(ans, solve1(V, X, r1, c1))

#        print kase, ans
        if ans >= 1e30:
            print "Case #%d: IMPOSSIBLE" % kase
        else:
            print "Case #%d: %.9f" % (kase, ans)
        sys.stdout.flush()

if __name__ == '__main__':
    main()

