
import random

def solve(W, L, A):
    res = []
    S = sorted(enumerate(A), key=lambda x: -x[1])
    trans = {}
    for i, x in enumerate(S):
        trans[i] = x[0]
        S[i] = x[1]
    R, x, y = [], 0, 0
    for i, r in enumerate(S):
        if not R:
            res.extend((x, y))
            R.append((x, r, r))
            x = r
        else:
            if W - x < r:
                break
            res.extend((x + r, y))
            R.append((x, r * 2, r))
            x += r * 2
    R.append((x, W - x, 0))
    R.append((W, 0, 0))
    level = R[0][2]
    while len(res) / 2 < len(A):
        Rn, x, y = [], 0, level
        for j in xrange(i, len(S)):
            r = S[j]
            if not Rn:
                res.extend((x, y + r))
                Rn.append((x, r, r * 2))
                x += r
            else:
                if W - x < r:
                    break
                res.extend((x + r, y + r))
                Rn.append((x, r * 2, r * 2 - (level - y)))
                x += r * 2
            for k in xrange(len(R)):
                if R[k][0] > x:
                    break
            red = R[0][2] - R[k - 1][2]
            y = level - red
        Rn.append((x, W - x, 0))
        Rn.append((W, 0, 0))
        R = Rn
        level += R[0][2]
        i = j
        if level > L:
            break
    while len(res) / 2 < len(A):
        x, y = random.randint(0, W), random.randint(0, L)
        for i in xrange(0, len(res), 2):
            dist = pow(pow(res[i] - x, 2) + pow(res[i + 1] - y, 2), 0.5)
            rsum = S[i / 2] + S[len(res) / 2]
            if dist < rsum:
                break
        else:
            res.append((x, y))
    xres = [0, 0] * len(A)
    for i in xrange(0, len(res), 2):
        pos = trans[i / 2] * 2
        xres[pos] = res[i]
        xres[pos + 1] = res[i + 1]
    return xres

def test(A, R):
    N = len(A)
    for i in xrange(0, N, 2):
        for j in xrange(i + 2, N, 2):
            dist = pow(pow(A[i] - A[j], 2) + pow(A[i + 1] - A[j + 1], 2), 0.5)
            rsum = R[i / 2] + R[j / 2]
            if dist < rsum:
                raise ValueError

def main(f):
    T = int(f.readline())
    for i in xrange(T):
        N, W, L = map(int, f.readline().split(' '))
        A = map(int, f.readline().split(' '))
        res = solve(W, L, A)
        print 'Case #%d: %s' % (i + 1, ' '.join(map(str, res)))
        test(res, A)

if __name__ == '__main__':
    import sys
    main(sys.stdin)
