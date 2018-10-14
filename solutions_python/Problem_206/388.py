import logging
import Queue as Q
import math
import pprint

logging.basicConfig(filename='log.txt', level=logging.DEBUG)

def compute(D,N,horses):
    max_time = -1
    for h in horses:
        if (D-h[0])*1.0/h[1] > max_time:
            max_time = (D-h[0])*1.0/h[1] 

    return D/max_time

t = int(raw_input())
for i in xrange(1, t + 1):
    logging.info("Solving case: {}".format(i))

    # N = int(raw_input())
    D, N = [int(x) for x in raw_input().split(" ")]
    horses = []
    for _ in xrange(N):
        horses.append([int(x) for x in raw_input().split(" ")])

    result = compute(D,N,horses)
    # correct_compute(grid)
    print "Case #{}: {:.6f}".format(i, result)
