import sys


def solve_cookies(farm_cost, farm_rate, target):
    time_spent = 0.0
    current_rate = 2.0
    while True:
        if target / current_rate < (farm_cost / current_rate + target / (current_rate + farm_rate)):
            return time_spent + target / current_rate
        else:
            time_spent += farm_cost / current_rate
            current_rate += farm_rate

nc = int(sys.stdin.readline())
for i in range(nc):
    f, c, x = map(float, sys.stdin.readline().split())
    print "Case #%s: %.7f" % (i + 1, solve_cookies(f, c, x))
