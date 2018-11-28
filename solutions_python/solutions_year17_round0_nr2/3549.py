dp = [[0]*10 for i in range(19)] # dp[i][j] = number of ways to make with i digits starting with j
for i in range(10):
    dp[0][i] = 1
for i in range(1, 19):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i-1][k]

def solve(n):
    n = str(n)
    numDigits = len(n)
    ans = ""
    for i in range(numDigits):
        s = n[-1*i - 1]
        a = int(s)
        if(ans != ""):
            b = int(ans[0])
        else:
            b = 9
        if(a > b):
            ans = str(a-1) + '9'*len(ans)
        else:
            ans = str(a) + ans
    while(ans[0] == '0'):
        ans = ans[1:]
    return ans
    
f = open("b.in")
t = int(f.readline())
for i in range(t):
    print "Case #" + str(i+1) + ": " + str(solve(int(f.readline())))
    