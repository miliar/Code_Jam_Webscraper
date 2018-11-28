import functools

def f(n,horses,dist):

    d = {}

    def recurse(current_city, current_horse, n, distance_left):
        if current_city == n - 1:
            return 0
        if (current_city, current_horse) in d:
            return d[(current_city, current_horse)]
        distance_to_go = dist[current_city]
        options = []
        if horses[current_city][0] >= distance_to_go:
            options.append(distance_to_go / horses[current_city][1] + recurse(current_city + 1,
                current_city, n, horses[current_city][0] - distance_to_go))

        if distance_left >= distance_to_go:
            options.append(distance_to_go / horses[current_horse][1] + recurse(current_city + 1,
                current_horse, n, distance_left - distance_to_go))
        d[(current_city, current_horse)] = min(options)
        return min(options)

    return recurse(0, 0, n, 0)

def recurse(current_city, current_horse, n):
    if current_city == n:
        return 0


T = int(input())
for case in range(1, T+1):
    n,q = map(int, input().split())
    horses = []
    for i in range(n):
        horses.append(list(map(int, input().split())))
    dist = []
    for i in range(n - 1):
        l = list(map(int, input().split()))
        dist.append(l[i+1])
    input()
    input()
    # print(n)
    ans = f(n,horses,dist)

    print("Case #%s: %s" % (case, ans))

