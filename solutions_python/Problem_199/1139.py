T = int(input())

def flip(S, k, start):
    for i in range(start, start + k):
        S[i] = (S[i] + 1) % 2

def solve(S,k):
    S = [0 if x == '-' else 1 for x in S]
    c = S.count(0)
    if c == 0:
        return 0
    else:
        first = S.index(0)
        if first > len(S) - k:
            return "IMPOSSIBLE"
        else:
            cnt = 0
            while True:
                flip(S,k,first)
                cnt += 1
                c = S.count(0)
                if c == 0:
                    return cnt
                else:
                    first = S.index(0)
                    if first > len(S) - k:
                        return "IMPOSSIBLE"

for i in range(1, T + 1):
    S,k = input().split()
    k = int(k)
    print("Case #{}: {}".format(i,solve(S,k)))
