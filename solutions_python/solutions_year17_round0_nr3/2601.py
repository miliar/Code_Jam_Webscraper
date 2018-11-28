def f(n, k):
    a = [n]
    for i in range(k):
        l = 0
        for p, x in enumerate(a):
            if x > l:
                l = x
                j = p
        left = (l - 1) // 2
        a[j] = left
        right = l - 1 - a[j]
        a.insert(j, right)
    res1 = max(left, right)
    res2 = min(left, right)
    return res1, res2


T = input()
T = int(T)
for t in range(1, T + 1):
    n, k = input().split()
    n = int(n)
    k = int(k)
    res1, res2 = f(n, k)
    print("Case #" + str(t) + ": " + str(res1) + " " + str(res2))
