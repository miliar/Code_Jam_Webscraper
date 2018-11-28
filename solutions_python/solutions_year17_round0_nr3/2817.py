def find(a):
    m, M, idx = -1, -1, -1
    for i in range(len(a)):
        if a[i] == 1:
            continue
        l = 0
        for j in range(i-1, -1, -1):
            if a[j] == 1:
                break
            l += 1
        r = 0
        for j in range(i+1, len(a)):
            if a[j] == 1:
                break
            r += 1
        mm = min(l,r)
        MM = max(l,r)
        if mm > m:
            m = mm
            M = MM
            idx = i
            continue
        if mm == m and MM > M:
            m = mm
            M = MM
            idx = i
    return m, M, idx

def solve(n, k):
    a = [0] * (n+2)
    a[0] = 1
    a[len(a)-1] = 1
    for i in range(k):
        m, M, idx = find(a)
        a[idx] = 1
    return "%d %d" % (M, m)

t = int(input())
for i in range(1, t + 1):
    n, k = input().split(" ")
    n = int(n)
    k = int(k)

    ret = solve(n, k)
    print ("Case #%d: %s" % (i, ret))

