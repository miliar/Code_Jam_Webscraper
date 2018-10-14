t = int(input())

for test in range(1, t+1):
    d, n = map(int, input().split())
    horses = []
    for i in range(n):
        k, s = map(int, input().split())
        horses.append((k, s))

    horses.sort(reverse=True)

    max_time = 0
    for h in horses:
        time = (d - h[0]) / h[1]
        max_time = max(max_time, time)

    print("Case #%d: %.6f" % (test, d / max_time))
