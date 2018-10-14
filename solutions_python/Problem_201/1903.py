import sys
import math

f = open(sys.argv[1])
t = f.readline()

o = open('o.txt', 'w')

for p in range(int(t)):

    l = f.readline()
    n, k = l.split(' ')
    n = int(n)
    k = int(k)
    s = [0 for _ in range(n + 2)]
    s[0] = s[len(s) - 1] = 1
    a = [s]
    y = 0
    z = 0

    while k > 0:

        b = 0
        c = 0

        for i, x in enumerate(a):
            if x.count(0) > c:
                c = x.count(0)
                b = i

        m = len(a[b]) // 2

        if len(a[b]) % 2 == 0:
            m -= 1

        a[b][m] = 1
        q = a[b][m:]
        w = a[b][:m + 1]
        ls = w.count(0)
        rs = q.count(0)
        y = max(ls, rs)
        z = min(ls, rs)
        a.insert(b + 1, q)
        a.insert(b + 1, w)
        del a[b]

        k -= 1

    for i, x in enumerate(a):
        if i != len(a) - 1:
            del x[len(x) - 1]

    o.write('Case #' + str(p+1) + ': ' + str(y) + ' ' + str(z) + '\n')

o.close()
