
def build(x, d):
    s = str(x)
    p = s[:-1] if d % 2 else s
    return pow(int(s + p), 2)

def check(x):
    s = str(x)
    n = len(s)
    return all(s[i] == s[n-i-1] for i in xrange(n / 2))

def solve(A, B):
    N, M = len(str(A)), len(str(B))
    Ns, Ms = (N + 1) / 2, (M + 1) / 2
    result = 0
    for Ds in xrange(Ns, Ms + 1):
        Dp = (Ds + 1) / 2
        Rl, Rh = pow(10, Dp - 1), pow(10, Dp)
        for x in xrange(Rl, Rh):
            xx = build(x, Ds)
            if xx < A: continue
            if xx > B: break
            if check(xx):
                result += 1
    return result

def main(f):
    T = int(f.readline())
    for i in xrange(T):
        A, B = map(int, f.readline().split(' '))
        print 'Case #%d:' % (i + 1), solve(A, B)

if __name__ == '__main__':
    import sys
    main(sys.stdin)
