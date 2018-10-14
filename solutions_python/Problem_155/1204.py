n = int(input())
for i in range(n):
    l, s = input().split()
    l = int(l)
    s = [int(el) for el in s]
    ans = 0
    standing = 0
    for j in range(l+1):
        diff = max(0, j - standing)
        standing += diff + s[j]
        ans += diff
    print("Case #{}: {}".format(i+1, ans))
