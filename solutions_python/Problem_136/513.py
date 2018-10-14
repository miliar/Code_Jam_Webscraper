__author__ = 'robertking'

from sys import stdin

data = (line for line in stdin.read().splitlines())

T = int(next(data))
for case in range(1, T + 1):
    C, F, X = map(float, next(data).split())
    cps = 2.0
    best = X / cps
    current_time = 0.0
    while True:
        buy_time = C / cps
        cps += F
        time_after_buy = X / cps
        if current_time + buy_time + time_after_buy > best:
            break
        else:
            best = current_time + buy_time + time_after_buy
        current_time += buy_time
    print "Case #%d: %s" % (case, best)


