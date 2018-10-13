def purge_horses(horses):
    horses.sort(key=lambda x: x[0])
    new_horses = []
    min_speed = horses[0][1]
    for idx in range(len(horses)):
        if horses[idx][1] <= min_speed:
            min_speed = horses[idx][1]
            new_horses.append(horses[idx])
    return new_horses

def A(n, d, horses):
    horses = purge_horses(horses)
    if len(horses) == 1 or horses[0][1] == horses[1][1]:
        k, s = horses[0]
        t = (d - k) / float(s)
        return d / t
    elif len(horses) == 2:
        x1, x2 = horses[0][0], horses[1][0]
        v1, v2 = horses[0][1], horses[1][1]
        t = (x1-x2) / float(v2-v1)
        if v1 * t > d - x1:
            t = (d - x1) / float(v1)
            return d / t
        else:
            meet = x1 + v1 * t
            t += ((d - meet) / float(v2))
            return d / t


def main():
    t = int(raw_input().strip())
    for i in xrange(t):
        d, n = map(int, raw_input().strip().split())
        horses = []
        for _ in range(n):
            k, s = map(int, raw_input().strip().split())
            horses.append((k, s))
        ans = A(n, d, horses)
        print "Case #%s: %f" % (i + 1, ans)

if __name__ == '__main__':
    main()
