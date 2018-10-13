# Python 3.2

from common import *

def main(casenum):
    n, v, x = readfloats()
    n = int(n + 0.5)
    v = int(v * 10000 + 0.5)
    x = int(x * 10000 + 0.5) * v

    r0 = [0] * n
    h0 = [0] * n
    temp = [0] * n
    for i in range(n):
        a, b = readfloats()
        temp[i] = (b, i)
        r0[i] = int(a * 10000 + 0.5)
        h0[i] = int(b * 10000 + 0.5) * r0[i]

    temp.sort()
    r = [0] * n
    h = [0] * n
    for i in range(n):
        r[i] = r0[temp[i][1]]
        h[i] = h0[temp[i][1]]

    if h[0] * v > x * r[0]:
        writecase(casenum, "IMPOSSIBLE")
        return
    if h[-1] * v < x * r[-1]:
        writecase(casenum, "IMPOSSIBLE")
        return

    cum_r = [0] * (n + 1)
    cum_h = [0] * (n + 1)
    for i in range(n):
        cum_r[i + 1] = cum_r[i] + r[i]
        cum_h[i + 1] = cum_h[i] + h[i]

    best = None
    for i in range(n):
        cur = None
        if i == 0:
            if r[i] * x == h[i] * v:
                cur = v / r[i]
        else:
            # print (i, cum_r[i], cum_h[i], r[i], h[i])
            d = r[i] * cum_h[i] - h[i] * cum_r[i]
            # print (d)
            if d == 0:
                if r[i] * x == h[i] * v:
                    cur = v / (cum_r[i + 1])
            else:
                a = (r[i] * x - h[i] * v) / d
                b = (v * cum_h[i] - x * cum_r[i]) / d
                # print (a, b)
                if (a >= 0) and (b >= 0):
                    cur = max(a, b)
                # print (cur)

        if cur is not None:
            # print (best, cur)
            if best is None:
                best = cur
            elif cur < best:
                best = cur

        cur = None
        if i + 1 == n:
            if r[i] * x == h[i] * v:
                cur = v / r[i]
        else:
            ch = cum_h[-1] - cum_h[i + 1]
            cr = cum_r[-1] - cum_r[i + 1]
            d = r[i] * ch - h[i] * cr
            if d == 0:
                if r[i] * x == h[i] * v:
                    cur = v / (r[i] + cr)
            else:
                a = (r[i] * x - h[i] * v) / d
                b = (v * ch - x * cr) / d
                if (a >= 0) and (b >= 0):
                    cur = max(a, b)

        if cur is not None:
            if best is None:
                best = cur
            elif cur < best:
                best = cur

    writecase(casenum, best)

run(main)
