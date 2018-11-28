import sys
sys.setrecursionlimit(100000)

def done(S):
    return all([x == '+' for x in S])

def flip(p, S, K):
    return S[0:p] + ''.join([('-' if x == '+' else '+') for x in S[p:p+K]]) + S[p+K:]

def solve(p, S, K, count):
    # print(p, S)
    if (p + K > len(S)):
        if done(S[p:]):
            return count
        else:
            return "IMPOSSIBLE"


    if done(S[p:p + K]):
        return solve(p + K, S, K, count)

    if (S[p] == '+'):
        return solve(p + 1, S, K, count)
    else:
        return solve(p + 1, flip(p, S, K), K, count+1)

T = int(input())
for i in range(1, T+1):
    S, K = input().split(' ')
    K = int(K)
    
    # print(S)
    res = solve(0, S, K, 0)

    print("Case #{}: {}".format(i, res))

