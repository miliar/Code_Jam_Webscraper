

from __future__ import division


t = int(raw_input())


for i in xrange(1, t + 1):
    d, n = [int(s) for s in raw_input().split(" ")]
    kisi = map(lambda el: (int(el[0]), int(el[1])), [raw_input().split(" ") for _ in xrange(n)])

    max_tim = 0
    for k, s in kisi:
        cur_tim = (d - k) / s
        if cur_tim > max_tim:
            max_tim = cur_tim

    print "Case #{0}: {1:.6f}".format(i, round(d / max_tim, 6))
