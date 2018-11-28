def solve(d, ride):
    minimun = 0
    for s, km in ride.items():
        time = (d - km) / s
        if time > minimun:
            minimun = time
    return d / minimun


t = int(input())
for i in range(1, t + 1):
    d, n = map(int, input().split())
    ride = {}
    for z in range(1, n + 1):
        k, s = map(int, input().split())
        km = ride.get(s)
        if not km or km > k:
            ride[s] = k
    print("Case #{}: {}".format(i, solve(d, ride)))
