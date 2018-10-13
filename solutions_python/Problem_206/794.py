def solve():
    d, n = map(int, input().split(" "))
    tmax = 0
    for _ in range(n):
        k, s = map(int, input().split(" "))
        tmax = max(tmax, (d - k) / s)
    return d / tmax

for i in range(int(input())):
    print(f"Case #{i+1}: {solve()}")
