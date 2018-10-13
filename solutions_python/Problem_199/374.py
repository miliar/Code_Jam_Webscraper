def all_happy(S):
    for p in S:
        if p == '-':
            return False
    return True

def flip(S, l, r):
    for i in range(l, r + 1):
        if S[i] == '+':
            S = S[:i] + '-' + S[i + 1:]
        else:
            S = S[:i] + '+' + S[i + 1:]
    return S

def count_flips(S, K):
    n = len(S)
    count = 0

    if K <= n:
        turn = True
        l = 0
        r = n - 1
        while True:
            if l >= r or all_happy(S):
                break
            if turn:
                if S[l] == '-' and (l + K - 1) < n:
                    S = flip(S, l, l + K - 1)
                    count += 1
                l += 1
            else:
                if S[r] == '-' and (r - K + 1) >= 0:
                    S = flip(S, r - K + 1, r)
                    count += 1

                r -= 1
            turn = not turn

    if all_happy(S):
        return count
    else:
        return 'IMPOSSIBLE'    

T = int(input())
for i in range(1, T + 1):
    S, k = [s for s in input().split(' ')]
    K = int(k)
    print("Case #{}: {}".format(i, count_flips(S, K)))
