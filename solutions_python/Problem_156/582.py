dp = [[0 for x in xrange(1001)] for y in xrange(1001)]

def calculate():
    for cnt in xrange(1001):
        for num in xrange(1, 1001):
            if cnt <= num:
                dp[cnt][num] = 0
            else:
                dp[cnt][num] = 1 + dp[cnt / 2][num] + dp[cnt - cnt / 2][num]
                dp[cnt][num] = min(dp[cnt][num], 1 + dp[cnt - num][num])

def solve(n, S):
    res = 1000
    for num in xrange(1, 1001):
        cur = 0
        for cnt in S:
            cur += dp[int(cnt)][num]
        res = min(res, cur + num)
    return res

if __name__ == '__main__':
    calculate()
    tests = int(raw_input());
    for test_id in xrange(1, tests + 1):
        n = int(raw_input())
        S = raw_input().split(' ')
        print 'Case #' + str(test_id) + ': ' + str(solve(n, S))

