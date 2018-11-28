import math

def solve(C, D, J, K):
    f = {}
    f[0] = [[10000] * 1442, [10000] * 1442]
    f[1] = [[10000] * 1442, [10000] * 1442]
    free = [[True] * 1440, [True] * 1440]
    for i, c in enumerate(C):
        for ii in range(c, D[i]):
            free[0][ii] = False
    for i, j in enumerate(J):
        for ii in range(j, K[i]):
            free[1][ii] = False
    p = 0
    for i in range(2):
        if free[i][0]:
            f[0][i][1] = 0
    for i in range(1, 1440):
        p = 1 - p
        # update
        for j in range(2):
            if not free[j][i]:
                for k in range(i + 1):
                    f[p][j][k] = 10000
                continue
            for k in range(1, i + 2):
                f[p][j][k] = min(f[1 - p][1 - j][i - k + 1] + 1, f[1 - p][j][k - 1])
    # print f[p]
    ans = min(f[p][0][720], f[p][1][720])
    if ans % 2:
        ans += 1
    return ans

def main():
    T = input()
    for i in xrange(1, T + 1):
        Ac, Aj = map(int, raw_input().strip().split())
        C = []
        D = []
        J = []
        K = []
        for _ in xrange(Ac):
            c, d = map(int, raw_input().strip().split())
            C.append(c)
            D.append(d)
        for _ in xrange(Aj):
            j, k = map(int, raw_input().strip().split())
            J.append(j)
            K.append(k)
        print 'Case #{0}: {1}'.format(i, solve(C, D, J, K))

if __name__ == '__main__':
    main()
