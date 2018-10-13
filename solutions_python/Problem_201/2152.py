def calc(N, K):
    MAX, MIN = 0, 0
    ds = [1] + [0]*N + [1]
    for _ in range(K):
        spot = float('inf')
        MAX, MIN = -1, -1
        for i in range(len(ds)):
            if ds[i] == 1:
                continue
            LS = RS = 0
            for j in range(i-1, -1, -1):
                if ds[j] == 1:
                    LS = i - j - 1
                    break
            for k in range(i+1, len(ds)):
                if ds[k] == 1:
                    RS = k - i - 1
                    break
            if min(LS, RS) > MIN:
                spot = i
                MIN = min(LS,RS)
                MAX = max(LS,RS)
            elif min(LS,RS) == MIN:
                if max(LS, RS) > MAX:
                    spot = i
                    MIN = min(LS, RS)
                    MAX = max(LS, RS)
        ds[spot] = 1
    return MAX,MIN


def inp(infile, outfile):
    with open(infile) as f, open(outfile, 'w') as g:
        T = int(f.readline())

        for i, _ in enumerate(range(T)):
            N, K = [int(x) for x in f.readline().split()]
            MAX, MIN = calc(N, K)
            print('Case #{}: {} {}'.format(i+1, MAX, MIN), file=g)

inp('/Users/Shmu/PycharmProjects/codejam_17/c_small1.txt',
    '/Users/Shmu/PycharmProjects/codejam_17/c_out1.txt')