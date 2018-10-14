
def similar(s, w, c):
    #print 'similar', s, w, c
    f = lambda x: x if x in c else '_'
    return map(f, s) == map(f, w)

def evaluate(idx, L, D):
    length = len(D[idx])
    R = filter(lambda s: len(s) == length, D)
    if len(R) == 1:
        return 0

    v = 0
    for i, c in enumerate(L):
        for w in R:
            if c in w:
                break
        else:
            continue

        #print 'c =', c, 'R =', R
        if c in D[idx]:
            R = filter(lambda s: similar(s, D[idx], L[:i+1]), R)
        else:
            v += 1
            R = filter(lambda s: c not in s, R)
        #print v, R
        if len(R) == 1:
            return v
    return v

def check(L, D):
    pos = -1
    value = -1
    for i in xrange(len(D)):
        v = evaluate(i, L, D)
        #print i, v
        if v > value:
            pos, value = i, v
    return D[pos]

def solve(data):
    D, Ls = data
    result = [check(L, D) for L in Ls]
    return ' '.join(result)

def get_input():
    N, M = map(int, raw_input().split())
    D = [raw_input() for i in xrange(N)]
    L = [raw_input() for i in xrange(M)]

    return D, L

def main():
    T = int(raw_input())
    for i in xrange(T):
        print 'Case #%d: %s' % (i + 1, solve(get_input()))

if __name__ == '__main__':
    main()
