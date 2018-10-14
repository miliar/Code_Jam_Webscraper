t = int(input())
for i in range(t):
    cnt1 = 0
    cnt2 = 0
    n = int(input())
    a = list(map(float, input().split()))
    a.sort()
    b = list(map(float, input().split()))
    b.sort()
    f = [False] * n
    cnt = 0
    for k in range(n):
        for j in range(n):
            if b[j] > a[k] and f[j] == False:
                f[j] = True
                cnt += 1
                break
    g = [False] * n
    cnt1 = 0
    for k in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if b[j] < a[k] and g[j] == False:
                g[j] = True
                cnt1 += 1
                break
    print('Case #',i + 1,':',' ',cnt1, ' ', n - cnt, sep = '')