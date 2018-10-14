# DEBUG = True
DEBUG = False

ncase = int(raw_input())

for cidx in range(ncase):
    tmp = map(int, raw_input().split())
    n = tmp[0]
    k = tmp[1]

    if DEBUG:
        print "n: {}, k: {}".format(n, k)

    if k == n:
        print "Case #{}: 0 0".format(cidx + 1)
        continue

    for i in range(64):
        if 2 ** i > k:
            level = i
            break

    s = []
    ss = []
    d = dict()
    for i in range(level):
        d[i] = dict()
        if len(s) == 0:
            x = n
            if (x - 1) % 2 == 0:
                t = (x - 1) / 2
                s.append(t)
                d[i][t] = 2
            else:
                t = x / 2
                s.append(t)
                s.append(t - 1)
                d[i][t] = 1
                d[i][t - 1] = 1
            if i == level - 2:
                ss = list(s)
            if DEBUG:
                print "i: {}, level: {}".format(i, level)
                print "s: {}".format(s)
                print "d: {}".format(d[i])
            continue

        tmp = []
        for x in s:
            if (x - 1) % 2 == 0:
                t = (x - 1) / 2
                if t not in tmp:
                    tmp.append(t)
                if t not in d[i]:
                    d[i][t] = 0
                # if DEBUG:
                    # print "i: {}, t: {}, x: {}, d: {}".format(i, t, x, d)
                d[i][t] += d[i - 1][x] * 2
            else:
                t = x / 2
                if t not in tmp:
                    tmp.append(t)
                if t not in d[i]:
                    d[i][t] = 0
                d[i][t] += d[i - 1][x]
                if t - 1 < 0:
                    continue
                if t - 1 not in tmp:
                    tmp.append(t - 1)
                if t - 1 not in d[i]:
                    d[i][t - 1] = 0
                d[i][t - 1] += d[i - 1][x]
        s = tmp
        if i == level - 2:
            ss = list(s)
        if DEBUG:
            print "i: {}, level: {}".format(i, level)
            print "s: {}".format(s)
            print "d: {}".format(d[i])

    tmp = k - 2 ** (level - 1)
    if DEBUG:
        print "k: {}, prev: {}, tmp: {}".format(k, 2 ** (level - 1), tmp)
    s.sort(reverse=True)
    ss.sort(reverse= True)
    if d.has_key(level - 2):
        for i in range(len(ss)):
            x = ss[i]
            if tmp >= d[level - 2][x]:
                tmp -= d[level - 2][x]
            else:
                if (x - 1) % 2 == 0:
                    t = (x - 1) / 2
                    s = [t, t]
                else:
                    t = x / 2
                    s = [t, t - 1]
                break

    print "Case #{}: {} {}".format(cidx + 1, max(s), min(s))
