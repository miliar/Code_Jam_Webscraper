import sys

__author__ = 'Oles Savluk'

def solve(s, k):
    N = len(s)
    ps = [v == '+' for v in s]
    count = 0
    for i in range(N):
        if not ps[i] and i+k <= N:
            count = count + 1
            for j in range(i, i+k):
                ps[j] = not ps[j]

    return count if all(ps) else 'IMPOSSIBLE'

# assert solve('-', 1) == 1
# assert solve('-+', 2) == 'IMPOSSIBLE'
# assert solve('-+-+-+-+', 2) == 4
# assert solve('-+-+-+-+', 3) == 'IMPOSSIBLE'

if __name__ == '__main__':
    lines = sys.stdin.readlines()

    T = int(lines[0].strip())
    it = 1
    for i in range(T):
        S, K = lines[it].strip().split(' ')
        K = int(K)
        it += 1
        print('Case #{}: {}'.format(i + 1, solve(S, K)))
