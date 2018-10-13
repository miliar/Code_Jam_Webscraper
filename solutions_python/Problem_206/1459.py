t = int(input())
for i in range(1, t+1):
    d, n = map(int, input().split())
    a = []
    for j in range(n):
        x, y = (map(int, input().split()))
        a.append((d-x)/y)
    print("Case #{}: {}".format(i, d/max(a)))



