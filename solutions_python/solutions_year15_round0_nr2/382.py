import sys
dp = []
for i in range(1050):
    dp.append([])
    for j in range(1050):
        dp[i].append(0)

for i in range(2,1050):
    for j in range(i):
        if j==0 or i==0:
            continue
        x = i/2
        y = i - x
        dp[i][j] = int(dp[x][j])+int(dp[y][j])+1
        if dp[i][j] > 1000:
            dp[i][j] = 1000


f = open('b.in','rb')
ca = int(f.readline())
for nu in range(ca):
    n = int(f.readline())
    a = f.readline().strip().split(' ')
    ans = 1000000
    for i in range(1001):
        if i == 0:
            continue
        res = i
        for data in a:
            data = int(data)
            if data > i:
                res += (data + i-1)/i -1
            
            
        if res < ans:
            ans = res
    print 'Case #%d: %d' %(nu+1,ans)

