t = int(raw_input())

d = {}

def atokey(a):
    return ','.join([str(x) for x in a])

def dup(v, t):
    global d

    if v % 2 == 0:
        t[v / 2] = t.get(v / 2, 0) + d[v]
        t[v / 2 - 1] = t.get(v / 2 - 1, 0) + d[v]

        key = atokey([v / 2, v / 2 - 1])
        t[key] = t.get(key, 0) + d[v]
        return [v / 2, v / 2 - 1]
    else:
        t[v / 2] = t.get(v / 2, 0) + d[v] * 2

        key = atokey([v / 2, v / 2])
        t[key] = t.get(key, 0) + d[v]
        return [v / 2]

def solve(n, k):
    global d

    d = dict()
    d[n] = 1
    i = 1
    s = {n}
    while True:
        l = list()
        dd = dict()
        for x in s:
            l += dup(x, dd)
        d = dd
        s = set(l)
        l = list(s)
        l.sort()

        if len(l) == 1:
            l.append(l[0])

        # print i, 'l', l, 'd', d

        if i * 2 > k:
            k -= i

            k -= d.get(atokey([l[1], l[1]]), 0)
            if k < 0:
                return [l[1], l[1]]

            k -= d.get(atokey([l[1], l[0]]), 0)
            if k < 0:
                return [l[1], l[0]]

            return [l[0], l[0]]

        i *= 2

for i in range(1, t + 1):
    n, k = [int(s) for s in raw_input().split(' ')]
    print('Case #{}: {}'.format(i, ' '.join([str(x) for x in solve(n, k)])))
