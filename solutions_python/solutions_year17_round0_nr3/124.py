from collections import defaultdict as dd


def show(i, val):
    print "Case #%s: %s %s" % (i, val[0], val[1])


def split(coll, total, count=None):
    if count is None:
        count = total
    rtotal = 0
    rcoll = dd(int)
    last_index = None
    skeys = sorted(coll.iterkeys(), reverse=True)
    lk = len(skeys)

    for i, key in enumerate(skeys):
        last_index = i
        v = coll[key]
        if v >= count:
            rtotal += v + count
            rcoll[key] += v - count
            nv = count
            count = 0
        else:
            rtotal += 2 * v
            count -= v
            nv = v
        
        if key == 2:
            rcoll[1] += nv
        elif key > 2:
            if key % 2 == 1:
                rcoll[key / 2] += 2 * nv
            else:
                rcoll[key / 2] += nv
                rcoll[key / 2 - 1] += nv

        if count == 0:
            break

    for i in xrange(last_index + 1, lk):
        rcoll[skeys[i]] = coll[skeys[i]]

    for key in rcoll.keys():
        if rcoll[key] == 0:
            del rcoll[key]

    return rcoll, rtotal


def sol(n, k):
    k -= 1
    if k == n - 1:
        return 0, 0

    coll = dd(int)
    coll[n] = 1
    total = 1

    while total <= k:
        k -= total
        coll, total = split(coll, total)

    if k > 0:
        coll, total = split(coll, total, k)

    minv, maxv = 0, 0
    l = max(coll.iterkeys())
    minv = (l - 1) / 2
    if l % 2 == 1:
        maxv = (l - 1) / 2
    else:
        maxv = (l - 1) / 2 + 1

    return maxv, minv


if __name__ == "__main__":
    T = int(raw_input().strip())

    for i in xrange(1, T + 1):
        n, k = map(int, raw_input().strip().split())
        show(i, sol(n, k))

