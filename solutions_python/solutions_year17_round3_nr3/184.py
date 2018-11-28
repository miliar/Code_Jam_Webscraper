from math import pi
def DEBUG(*args):
    pass
    # print args

EPS = 1e-10

def calc(Ps):
    r = 1.0
    for p in Ps:
        r *= p
    return r

def solve(N, K, U, Ps):
    assert (N==K)
    Ps = sorted(Ps)
    cPs = [1-p for p in Ps]
    i = 0
    DEBUG('input', N, K, U, Ps)
    while True:
        if i == N:
            p = 1.0
        else:
            p = Ps[i]
        s = 0
        for j in range(i):
            s += p-Ps[j]
        DEBUG(i, s, EPS, U, '!')
        if s + EPS > U:
            DEBUG('!!')
            break
        if i == N: break
        i += 1
    for j in range(i):
        Ps[j] = p-(s-U)/float(i)
    DEBUG(N, K, U, Ps, p, s)
    return calc(Ps)

def main():
    T = input()

    for i in range(T):
        N, K = map(int, raw_input().split())
        U = input()
        Ps = map(float, raw_input().split())
        print 'Case #%d: %.6f' % ((i+1), solve(N, K, U, Ps))

main()
