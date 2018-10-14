def horse_time(horses, dest):
    horses.sort(key=lambda a: a[0])
    # print ('horses', horses)
    walks = list()
    walks.append([dest, horses[0][1], horses[0][0]])

    for i in range(1, len(horses)):
        # print ('walks', walks)
        k1, s1 = walks[-1][2], walks[-1][1]
        k2, s2 = horses[i]
        m = meet(k1, k2, s1, s2)
        # print("MMM", m)
        if m < walks[-1][0]:
            walks[-1][0] = m
        elif m < dest:
            walks.append([m, s2, k2])

    walks.append((dest, horses[-1][1]))
    # print(walks)
    st = horses[0][0]
    t = 0.

    for w in walks:
        k, s = w[0], w[1]
        d = k-st
        t += d / s
        st = k


    return t



def meet(k1, k2, s1, s2):
    if s1>s2:
        return (k1*s2 - k2*s1) / (s2 - s1)
    else:
        return 2**31


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    d, n = map(int, input().split())
    d = float(d)
    horses = list()
    for _ in range(n):
        parsed = input().split()
        k, s = float(parsed[0]), float(parsed[1])
        horses.append((k, s))

    t = horse_time(horses, d)

    spd = d / t
    print("Case #{}: {} ".format(i, str(spd)))





