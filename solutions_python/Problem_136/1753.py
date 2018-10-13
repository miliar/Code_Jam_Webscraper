
import sys
import math

class CookieFactory:

    def __init__(self, farm_cost, farm_util):
        self.farm_cost = farm_cost
        self.farm_util = farm_util

        self.curr_time = 0.0
        self.curr_rate = 2.0        # 2 cookies per second
        self.num_cookies = 0        # start with none

    def get_time_til_have(self, target):
        """
        Given the number of cookies we currently have, and the rate
        at which we produce them, find the amount of time necessary
        to produce TARGET number of cookies.

        Returns in absolute time.
        """

        if self.num_cookies > target:
            return 0.0      # no time needed

        needed = (target - self.num_cookies)
        return (needed / self.curr_rate) + self.curr_time

    def produce_cookies(self, time_elapsed):
        """
        Produces cookies for the specified amount of time.
        """

        # self.num_cookies += math.ceil(self.curr_rate * time_elapsed)
        self.num_cookies += self.curr_rate * time_elapsed
        self.curr_time += time_elapsed

    def buy_farm(self):
        # assert self.num_cookies >= self.farm_cost, 'not enough cookies!'

        # self.num_cookies -= self.farm_cost
        self.num_cookies = 0        # always buy farms as early as possible
        self.curr_rate += self.farm_util

def compute_time(factory, goal, num_extra_farms=0):
    for _ in xrange(num_extra_farms):
        time = factory.get_time_til_have(factory.farm_cost)
        factory.produce_cookies(time - factory.curr_time)
        factory.buy_farm()
    return factory.get_time_til_have(goal)

def compute_shortest_time(farm_cost, farm_util, goal):
    best = compute_time(CookieFactory(farm_cost, farm_util), goal)

    num_extra_farms = 1
    while True:
        factory = CookieFactory(farm_cost, farm_util)
        time = compute_time(factory, goal, num_extra_farms)

        if time > best:
            break

        best = time
        num_extra_farms += 1

    return best

if __name__ == '__main__':

    num_cases = int(sys.stdin.readline())

    for i in xrange(1, num_cases + 1):
        line = sys.stdin.readline()
        [farm_cost, farm_util, goal] = [float(x) for x in line.split()]

        time = compute_shortest_time(farm_cost, farm_util, goal)

        print 'Case #%d: %.7f' % (i, time)
