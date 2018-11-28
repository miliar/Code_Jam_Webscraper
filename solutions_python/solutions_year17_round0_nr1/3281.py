
d = {}
def solve(s):
    t = tuple(s)
    if t in d: return d[t]
    d[t] = float('inf')
    # print(s)
    for i in s:
        if i == False: break
    else:
        d[t] = 0
        return 0

    res = float('inf')
    for i in range(len(s) - K + 1):

        for k in range(K):
            s[i+k] = 1- s[i+k]

        res = min(solve(s) + 1, res)

        for k in range(K):
            s[i+k] = 1- s[i+k]

    d[t] = res
    # print(s, res)
    return res


T = int(input())

for t in range(1,T+1):
    d = {}
    S, K = input().split()
    # print(S,K)
    K = int(K)
    S = list(map(lambda x: 0 if x == '-' else 1, S))

    res = solve(S)
    if res == float('inf'): res = 'IMPOSSIBLE'
    print("Case #{}: {}".format(t,res))
