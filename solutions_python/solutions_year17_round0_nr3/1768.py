

# def compute(occupied, n):
#     emptiesl = {0: 0}
#     emptiesr = {n-1: 0}
#     for i in range(1, n):
#         if not occupied[i-1]:
#             emptiesl[i] = emptiesl[i-1] + 1
#         else:
#             emptiesl[i] = emptiesl[i-1]
#
#     for i in range(n-2, -1, -1):
#         if not occupied[i+1]:
#             emptiesr[i] = emptiesr[i+1] + 1
#         else:
#             emptiesr[i] = emptiesr[i+1]
#
#     return emptiesl, emptiesr

def compute(occupied, n):
    el = {0: 0, 1: 0}
    er = {n-1: 0, n-2: 0}

    for i in range(2, n):
        el[i] = 0 if occupied[i-1] else el[i-1] + 1

    for i in range(n-3, -1, -1):
        er[i] = 0 if occupied[i+1] else er[i+1] + 1

    return el, er

def consider(occupied, n, el, er):
    d = {i: min(el[i], er[i]) for i in range(n) if not occupied[i]}

    m = max(d.values())
    s = list()

    for i, x in d.iteritems():
        if x == m:
            s.append(i)

    return s


def choose(s, el, er):
    if len(s) == 1:
        return s.pop()

    d = {x: max(el[x], er[x]) for x in s}
    m = max(d.values())

    for x in s:
        if d[x] == m:
            return x


case = 1
for _ in range(int(raw_input())):
    mem = dict()

    n, k = raw_input().split()
    n, k = int(n) + 2, int(k)
    if n == k:
        y, z = 0, 0
    else:
        occupied = [False for i in range(n)]
        occupied[0] = occupied[n-1] = True

        for p in range(k):
            el, er = compute(occupied, n)
            s = consider(occupied, n, el, er)
            chosen = choose(s, el, er)
            occupied[chosen] = True

        el, er = compute(occupied, n)
        y, z = max(el[chosen], er[chosen]), min(el[chosen], er[chosen])

    # print occupied
    print 'Case #{0}: {1} {2}'.format(case, y, z)
    case += 1
