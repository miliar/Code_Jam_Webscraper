def blade(x, y, k):
    if x + k > X or y + k > Y:
        return False

    if k % 2 == 1:
        cx = x + k / 2
        cy = y + k / 2
        cx += 0.5
        cy += 0.5
    else:
        cx = x + k / 2
        cy = y + k / 2

    mx = 0
    my = 0
    for i in xrange(y, y + k):
        for j in xrange(x, x + k):
            if ((i == y and (j == x or j == x + k - 1)) or
                (i == y + k - 1 and (j == x or j == x + k - 1))):
                continue
            mx += (2 * j + 1 - 2 * cx) * (D + M[i][j])
            my += (2 * i + 1 - 2 * cy) * (D + M[i][j])

    return mx == 0 and my == 0

if __name__ == '__main__':
    for caseno in xrange(int(raw_input())):
        Y, X, D = [int(s) for s in raw_input().split()]
        M = []
        for _ in xrange(Y):
            row = [int(ch) for ch in raw_input()]
            M += [row]

        best = None
        for y in xrange(0, Y):
            for x in xrange(0, X):
                for k in xrange(min(X, Y), 2, -1):
                    if best and k <= best: break
                    if blade(x, y, k):
                        best = k
                        break

        res = str(best) if best else 'IMPOSSIBLE'
        print 'Case #%d: %s' % (caseno + 1, res)
