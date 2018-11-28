# -*- coding: utf-8 -*-
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
  return a * b / gcd (a, b)


def choose_barber(place, barbers_cost):
    leave_time = [2] * len(barbers_cost)
    next_barber = -1

    lcm_num = 1
    for i in barbers_cost:
        lcm_num = lcm(lcm_num, i)

    round_cost = sum(map(lambda n:lcm_num/n, barbers_cost))

    for i in xrange((place-1) % round_cost + 1):
	leave_time = map(lambda n:n-min(leave_time), leave_time)
	next_barber = leave_time.index(min(leave_time))
        leave_time[next_barber] = barbers_cost[next_barber]
    return next_barber + 1

if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    test_num = int(f.readline())

    for i in xrange(1, test_num+1):
        test_data = map(int, f.readline().split())
        barbers_cost = map(int, f.readline().split())
        ans = choose_barber(test_data[1], barbers_cost)
        print('Case #%i: %s' % (i, ans) )
