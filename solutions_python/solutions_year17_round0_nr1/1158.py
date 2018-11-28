import fileinput
from functools import reduce
from operator import concat

def solve(S, K):
    y = 0
    for i in range(0, len(S)-1):
        if i + K > len(S):
            break
        s = S[i]
        if s == '-':
            S = S[0:i] + reduce(concat, map(lambda c: '+' if c == '-' else '-', S[i:i+K])) + S[i+K:len(S)]
            # print(S)
            y += 1
        if not '-' in S:
            return y
    return 'IMPOSSIBLE'

f = fileinput.input()
T = int(f.readline())
for case in range(1, T+1):
    S, K = f.readline().split()
    # print(S, K)
    solution = solve(S, int(K))
    print("Case #{0}: {1}".format(case, solution))
