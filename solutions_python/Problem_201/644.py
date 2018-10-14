Cases = int(input())
for Case in range(Cases):
    n, k = list(map(int, input().split()))
    
    segs = [n]
    for i in range(k):
        m = max(segs)
        for j in range(i):
            if segs[j] == m:
                segs[j] = (m-1) // 2
                segs.append(m // 2)
                break
    u = max(segs)

    print('Case #%d: %d %d' % (Case+1, u//2, (u-1)//2))