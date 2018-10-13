
def tograph():
    # transform intro a graph:
    # we create an edge 
    pass


def small(n, q, e, s, u, v):
    # for town look at the smallest time we can be there
    first = {0: 0.0}

    # we are at city - 1
    for city in range(n):

        # use the given horse
        next_time = first[city]

        horse_remaining = e[city]
        next_city = city + 1

        while next_city < n and d[next_city-1][next_city] <= horse_remaining:

            horse_remaining -= d[next_city-1][next_city]
            next_time = next_time + ( d[next_city-1][next_city] / s[city] )

            if next_city not in first:
                first[next_city] = next_time
            else:
                first[next_city] = min(first[next_city], next_time)

            next_city += 1

    return first[n-1]


T = int(raw_input().strip())
for t in range(1, T+1):

    n, q = map(int, raw_input().strip().split(' '))
    e, s = [], []
    for _ in range(n):
        e_, s_ = map(float, raw_input().strip().split(' '))
        e.append(e_)
        s.append(s_)

    d = []
    for _ in range(n):
        d.append(map(float, raw_input().strip().split(' ')))

    u, v = [], []
    for _ in range(q):
        u_, v_ = map(int, raw_input().strip().split(' '))
        u.append(u_)
        v.append(v_)

    sol = small(n, q, e, s, u, v)

    print "Case #{}: {}".format(t, sol)
