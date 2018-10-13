# -*- coding: utf-8 -*-

from __future__ import print_function

time_to_get = lambda missing, speed: round(missing / speed, 7)

def round_all(precision):
    def decorator(function):
        def _rounding(*args, **kwargs):
            return tuple(round(res, precision) for res in function(*args, **kwargs))
        return _rounding
    return decorator

def go(farm_price, speed_inc, winning_amount):
    speed = 2.0
    amount = 0.0
    time_spend = 0.0

    def is_it_worth_to_buy_a_farm(missing):
        if missing <= farm_price:
            return False

        speed_after_buying = speed + speed_inc
        return time_to_get(farm_price, speed) + time_to_get(winning_amount, speed_after_buying) < time_to_get(missing, speed)

    @round_all(7)
    def buy_farm():
        return 0.0, time_spend + time_to_get(farm_price, speed), speed + speed_inc
    
    while winning_amount > amount:
        missing = winning_amount - amount

        if is_it_worth_to_buy_a_farm(missing):
            amount, time_spend, speed = buy_farm()
        else:
            return time_spend + time_to_get(missing, speed)


if __name__ == '__main__':
    import sys
    num = int(sys.stdin.readline())

    for i in xrange(1, num + 1):
        farm_price, speed_inc, winning_amount = (float(part) for part in sys.stdin.readline().split())
        print("Case #%d: %.7f" % (i, go(farm_price, speed_inc, winning_amount)))


import unittest

class Test(unittest.TestCase):

    def test_round_all(self):
        @round_all(1)
        def x():
            return (1.11,)

        self.assertEqual((1.1,), x())

    def test_all(self):
        data = (
            ((500.0, 4.0, 2000.0), 526.1904762),
            ((30.0, 1.0, 2.0), 1.0),
            ((30.0, 2.0, 100.0), 39.1666667),
            ((30.50000, 3.14159, 1999.19990), 63.9680013),
        )

        for args, expected in data:
            self.assertEqual(expected, go(*args))

    def test_time_to_end(self):
        data = (
            (100.0, 5.0, 20.0),
            (1.0, 2.0, 0.5),
        )
        for missing, speed, expected in data:
            self.assertEqual(expected, time_to_get(missing, speed))
