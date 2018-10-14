def do_task():
    d, n = map(int, input().split())
    time = 0
    for i in range(n):
        k, s = map(int, input().split())
        time = max(time, (d - k) / s)
    return float(d / time)

t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i + 1, do_task()))