import sys

def solve(S, K):
    flips = 0
    for i in range(len(S)-K+1):
        if S[i] != '+':
            for j in range(K):
                S[i+j] = '-' if S[i+j] == '+' else '+'
            flips += 1
    return flips if all((p == '+' for p in S)) else 'IMPOSSIBLE'

for t in range(1, int(input()) + 1):
    S, K = sys.stdin.readline().split()
    print("Case #{}: {}".format(t, solve(list(S), int(K))))
