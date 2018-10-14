f = open("C-small-attempt0.in")

def input2():
       res = f.readline()
       return res

def get_next_city(city_from):
    # for small +1 is enough
    city_to = city_from + 1

    distance = G[city_from][0][1]

    return city_to, distance



def get_min_time(city, target_city, horse):
    if (city, target_city, horse) in cache:
        return cache[(city, target_city, horse)]

    if city == target_city:
        return 0
    else:

        next_city, next_city_dist = get_next_city(city)

        endurance, speed = horses[city - 1]
        if endurance >= next_city_dist:
            change_res = next_city_dist / speed + get_min_time(next_city, target_city, (endurance - next_city_dist, speed))
        else:
            change_res = MAX_INT

        endurance, speed = horse
        if endurance >= next_city_dist:
            not_change_res = next_city_dist / speed + get_min_time(next_city, target_city, (endurance - next_city_dist, speed))
        else:
            not_change_res = MAX_INT

        res = min(change_res, not_change_res)
        cache[(city, target_city, horse)] = res
        return res

MAX_INT = 10 ** 20
T = int(input().strip())

for t in range(T):
    N, Q = [int(x) for x in input().strip().split(' ')]

    horses = [None] * N                 # array of pairs (endurance, velocity)
    for h in range(N):
        horses[h] = tuple(int(x) for x in input().strip().split(' '))

    # read G
    G = [None] * (N + 1)

    # CONSIDER keeping adjacency matrix if for FW it's better
    for i in range(N):
        roads = [int(x) for x in input().strip().split(' ')]
        for ri, r in enumerate(roads):
            city_from, city_to = i + 1, ri + 1

            if G[city_from] is None:
                G[city_from] = []
            if r != -1:
                G[city_from].append((city_to, r))

    # do FW
    ...

    # read Qs
    res = []
    for q in range(Q):
        city_from, city_to = [int(x) for x in input().strip().split(' ')]

        # or instead of FW do dijkstra here

        cache = {}
        res.append(str(get_min_time(city_from, city_to, horses[0])))

    # CONSIDER single res!
    print("Case #{}: {}".format(t + 1, ' '.join(res)))