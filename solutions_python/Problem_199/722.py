opposite = {'+': '-', '-': '+'}


def solve(s, K):
    s = list(s)
    i = cnt = i = 0
    while i <= len(s)-K:
        while s[i] == '+' and i <= len(s) - K:
            i += 1
        if i <= len(s) - K:
            cnt += 1
            for j in xrange(i, i+K):
                s[j] = opposite[s[j]]
        i += 1
    if all(map(lambda x: x == '+', s)):
        return cnt
    else:
        return "IMPOSSIBLE"



for qq in xrange(1, int(raw_input())+1):
    s, K = raw_input().split()
    K = int(K)
    ans = solve(s, K)
    print 'Case #{}: {}'.format(qq, ans)
