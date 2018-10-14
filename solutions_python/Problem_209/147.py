from  math import pi

f = open('ans.txt', 'w')

c = int(input())
for i in range(1,c+1):
    n, k = map(int, input().split())
    pancakes = []
    pancakes2 = []

    for j in range(n):
        r, h = map(int, input().split())
        pancakes.append((r, h*2*pi*r, h, j))
        pancakes2.append((h*2*pi*r, r, h, j))
    pancakes.sort(reverse=True)
    pancakes2.sort(reverse=True)
    m = 0
    for l in range(n-k+1):
        ans = 0
        ans += pi*(pancakes[l][0]**2)
        ans += pancakes[l][1]
        t = k-1
        for u in range(n):
            if not t:
                break
            if pancakes2[u][1] <= pancakes[l][0] and pancakes2[u][3] != pancakes[l][3]:
                ans += pancakes2[u][0]
                t-=1
        m = max(m, ans)
    f.write(f"Case #{i}: {m}\n")
f.close()