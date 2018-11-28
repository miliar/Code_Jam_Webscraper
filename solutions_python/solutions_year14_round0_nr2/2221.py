import sys

inp = sys.stdin.read().split("\n")
cases = int(inp.pop(0))


def best(rate, boost, goal, cost):
    waitprice = goal/rate
    buyprice = cost / rate
    if waitprice < buyprice + goal / (rate+boost):
        return waitprice
    return buyprice + best(rate + boost, boost, goal, cost)

for case in range(cases):
    cost, boost, goal = tuple(float(i) for i in inp.pop(0).split())
    rate = 2
    #seconds = best(rate, boost, goal, cost)
    seconds = 0
    waitprice = goal/rate
    buyprice = cost / rate
    while waitprice >= buyprice + goal / (rate + boost):
        seconds += buyprice
        rate += boost
        waitprice = goal/rate
        buyprice = cost / rate
    seconds += waitprice
    print("Case #%d: %.7f" % (case + 1, seconds))
