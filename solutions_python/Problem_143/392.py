n = int(input())

for i in range(n):
    a, b, k = map(int, input().split())
    count = sum(1 for i in range(a) for j in range(b) if i & j < k)
    print("Case #{}: {}".format((i+1), count))
