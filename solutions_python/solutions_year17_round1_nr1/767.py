T = int(input())
for t in range(1,T+1):
    used = set()
    n, m = map(int, input().split())
    L = [[c for c in input()] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if L[i][j] != '?' and L[i][j] not in used:
                i2, j2 = i, m-1
                i3, j3 = i, 0
                c = L[i][j]
                y = j
                while y+1 < m and L[i][y+1] == '?':
                    y += 1
                j2 = y
                y = j
                while y-1 >= 0 and L[i][y-1] == '?':
                    y-=1
                j3 = y
                while i2+1 < n and L[i2+1][j] == '?':
                    k = j
                    i2 += 1
                    while k+1 < m and L[i2][k+1] == '?':
                        k += 1
                    j2 = min(k, j2)
                    k = j
                    while k-1 >= 0 and L[i2][k-1] == '?':
                        k -= 1
                    j3 = max(k, j3)
                while i3-1 >= 0 and L[i3-1][j] == '?':
                    k = j
                    i3 -= 1
                    while k-1 >= 0 and L[i3][k-1] == '?':
                        k -= 1
                    j3 = max(k, j3)
                    k = j
                    while k+1 < m and L[i3][k+1] == '?':
                        k+=1
                    j2 = min(j2, k)
                i4, j4 = i, j
                i5, j5 = i, j
                c = L[i][j]
                y = i
                while y+1 < n and L[y+1][j] == '?':
                    y += 1
                i4 = y
                y = i
                while y-1 >= 0 and L[y-1][j] == '?':
                    y-=1
                i5 = y
                while j4+1 < m and L[i][j4+1] == '?':
                    k = i
                    j4 += 1
                    while k+1 < n and L[k+1][j4] == '?':
                        k += 1
                    i4 = min(k, i4)
                    k = i
                    while k-1 >= 0 and L[k-1][j4] == '?':
                        k -= 1
                    i5 = max(k, i5)
                while j5-1 >= 0 and L[i][j5-1] == '?':
                    k = i
                    j5 -= 1
                    while k-1 >= 0 and L[k-1][j5] == '?':
                        k -= 1
                    i5 = max(k, i5)
                    k = i
                    while k+1 < n and L[k+1][j5] == '?':
                        k+=1
                    i4 = min(i4, k)
                if (i2-i3+1)*(j2-j3+1) < (i4-i5+1)*(j4-j5+1):
                    i2, i3, j2, j3 = i4, i5, j4, j5
                for x in range(i3, i2+1):
                    for y in range(j3, j2+1):
                        assert(L[x][y] == '?' if x != i or y != j else True)
                        L[x][y] = c
                used.add(c)
    print("Case #%d:" %t)
    for l in L:
        print(''.join(l))
                    
