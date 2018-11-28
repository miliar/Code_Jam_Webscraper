def check(mp, n, m):
    colMax = [100] * m
    for i in range(n):
        vis = [0] * m
        maxVal = max(mp[i])
        for j in range(m):
            if mp[i][j] != maxVal:
                colMax[j] = min(mp[i][j], colMax[j])
    # print('colMax:', colMax)
    for i in range(n):
        for j in range(m):
            if mp[i][j] > colMax[j]:
                return False
    return True
for t in range(int(input())): 
    n, m = map(int, input().split())
    mp = []
    for i in range(n):
        mp.append(list(map(int, input().split())))
    ans = 'YES' if check(mp, n, m) else 'NO'
    print('Case #{}: {}'.format(t + 1, ans))
