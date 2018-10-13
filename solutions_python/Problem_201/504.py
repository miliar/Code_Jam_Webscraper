import sys

__author__ = 'Oles Savluk'

def solve(n, k):
    vc = {}
    vc[n] = 1
    res = n // 2, (n - 1) // 2
    while k > 0:
        v = max(vc.keys())
        c = vc[v]
        k = k - c
        res = v // 2, (v - 1) // 2
        for i in res:
            if i > 0:
                if i not in vc:
                    vc[i] = 0
                vc[i] = vc[i] + c
        del vc[v]
    return res

# assert solve(1, 1) == (0, 0)
# assert solve(2, 1) == (1, 0)
# assert solve(3, 1) == (1, 1)
# assert solve(4, 4) == (0, 0)
# assert solve(10**18, 10**18) == (0, 0)

if __name__ == '__main__':
    lines = sys.stdin.readlines()

    T = int(lines[0].strip())
    it = 1
    for i in range(T):
        N, K = [int(v) for v in lines[it].strip().split(' ')]
        it += 1
        l,r = solve(N, K)
        print('Case #{}: {} {}'.format(i + 1, l, r))
