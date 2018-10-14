from math import ceil
from math import floor

T = int(raw_input(""))

def fon(n, k):
    if k == 0: return [n]
    return fon(floor(n/2), floor((k-1)/2)) + fon( ceil(n/2), ceil((k-1)/2) )

for o in range(1, T+1):
    N, K = [int(x) for x in raw_input("").split(" ")]

    queue = [float(N)]

    la, lb, lv = None, None, None

    while K > 0:
        v, queue = queue[0], queue[1:]

        a = ceil(v/2)-1
        b = v-1-a

        la, lb, lv = a, b, v

        queue.append(max([la, lb]))
        queue.append(min([la, lb]))

        K -= 1

        queue.sort(reverse = True)
    # print lv

    # la -=1
    # lb -=1

    # la = floor(lv/2)
    # lb = ceil(lv/2)

    a, b = max([la, lb]), min([la, lb])
    # print queue
    print "Case #%d: %d %d" % (o, a, b)
