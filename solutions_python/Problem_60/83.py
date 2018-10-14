
class Chick(object):
    def __init__(self, x, v):
        super(Chick, self).__init__()
        self.x = x
        self.v = v

    def check(self, B, T):
        self.ok = self.x + T * self.v >= B

def solve():
    N, K, B, T = map(int, raw_input().split(' '))
    X = map(int, raw_input().split(' '))
    V = map(int, raw_input().split(' '))

    chicks = [Chick(X[i], V[i]) for i in xrange(N)]
    for c in chicks:
        c.check(B, T)
    if len(filter(lambda c: c.ok, chicks)) < K:
        return 'IMPOSSIBLE'

    ok = 0
    count = 0
    for i in xrange(N - 1, -1, -1):
        if ok == K: break
        if chicks[i].ok:
            ok += 1
        else:
            count += K - ok

    return count

def main():
    T = int(raw_input())
    for i in xrange(T):
        print 'Case #%s: %s' % (i + 1, solve())

if __name__ == '__main__':
    main()
