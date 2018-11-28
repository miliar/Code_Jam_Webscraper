__author__ = 'alestainer'

from math import log, floor, ceil

def max_and_min(n, k):
    splits = 2 ** floor(log(k, 2))
    left = n - splits + 1
    to_distribute = k - splits + 1
    if (to_distribute <= ((left) % splits)):
        if (((n - splits + 1) // splits + 1) % 2 == 1):
            return (left // splits + 1) // 2, (left // splits + 1) // 2
        else:
            return (left // splits + 1) // 2, (left // splits + 1) // 2 - 1
    else:
        if ((left // splits ) % 2 == 1):
            return (left // splits) // 2, (left // splits) // 2
        else:
            return (left // splits) // 2, (left // splits) // 2 - 1

t = int(raw_input())
for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]
    right, left = max_and_min(n=n, k=k)
    print "Case #{}: {} {}".format(i, int(right), int(left))
