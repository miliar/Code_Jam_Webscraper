# 0: 1
# 1: -1
# 2: i
# 3: -i
# 4: j
# 5: -j
# 6: k
# 7: -k

def mul(a, b):
    return [
        [0, 1, 2, 3, 4, 5, 6, 7],
        [1, 0, 3, 2, 5, 4, 7, 6],
        [2, 3, 1, 0, 6, 7, 5, 4],
        [3, 2, 0, 1, 7, 6, 4, 5],
        [4, 5, 7, 6, 1, 0, 2, 3],
        [5, 4, 6, 7, 0, 1, 3, 2],
        [6, 7, 4, 5, 3, 2, 1, 0],
        [7, 6, 5, 4, 2, 3, 0, 1],
    ][a][b]

def solve():
    l, x = map(int, input().split())
    s = input() * x
    s = list(map((lambda x: {'i':2, 'j':4, 'k':6}[x]), s))
    dp = [[[False]*8 for i in range(len(s))] for j in range(3)]
    dp[0][0][s[0]] = True
    for i in range(1, len(s)):
        for prev in range(8):
            for seg in range(3):
                if dp[seg][i-1][prev]:
                    dp[seg][i][mul(prev, s[i])] = True
        if dp[0][i-1][2]:
            dp[1][i][s[i]] = True
        if dp[1][i-1][4]:
            dp[2][i][s[i]] = True
    return 'YES' if dp[2][-1][6] else 'NO'

T = int(input())

for test in range(T):
    print("Case #%d: %s" % (test+1, solve()))


