T = int(input())

for case in range(T):
    d, n = map(int, input().split(" "))

    max_time = 0

    for _ in range(n):
        k, s = map(int, input().split(" "))
        time = (d - k) / s
        max_time = max(max_time, time)

    v = d / (max_time * 1.0)
    print("Case #%d: %.6f" % (case + 1, v))
