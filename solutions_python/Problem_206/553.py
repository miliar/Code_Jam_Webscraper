def findTime(d, horses):
    max_time = float(0)
    for i in horses:
        dist = d - i[0]
        speed = i[1]
        time = dist/speed
        max_time = max(max_time, time)

    req = d/max_time
    return req

t = int(input())
i = 0

while t:
    t -= 1
    i += 1

    d, n = map(int, input().split())

    horses = []
    for _ in range(n):
        horses.append(list(map(int, input().split())))



    print("Case #{}: {:.6f}".format(i, findTime(d, horses)))
