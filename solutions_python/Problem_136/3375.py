#!/usr/bin/env python3
import sys
import os
import logging


class CookieClicker:
    def _resolve(self, farm_cost, farm_gain_rate, target_cookies, gain_rate=2.0):
        # the required time if we dont buy the farm
        no_farm_time = target_cookies / gain_rate

        get_farm_time = farm_cost / gain_rate

        if get_farm_time + target_cookies / (gain_rate + farm_gain_rate) < no_farm_time:
            return get_farm_time + self._resolve(farm_cost, farm_gain_rate, target_cookies, gain_rate + farm_gain_rate)

        return no_farm_time

    def run(self, filename):
        if not os.path.exists(filename):
            raise IOError("file does not exists")

        with open(filename) as f:
            n_test_case = int(f.readline().rstrip())

            logging.debug("N of Test case: %d", n_test_case)
            sys.setrecursionlimit(6000)

            for x in range(0, n_test_case):
                (farm_cost, farm_gain_rate, target_cookies) = f.readline().rstrip().split()
                win_seconds = self._resolve(float(farm_cost), float(farm_gain_rate), float(target_cookies))

                logging.debug("farm_cost: %s, farm_gain_rate: %s, target_cookies: %s" %
                      (farm_cost, farm_gain_rate, target_cookies))
                print("Case #%d: %.7f" % (x + 1, win_seconds))




logging.basicConfig(level=logging.WARN)
if len(sys.argv) <= 1:
    exit("Usage: python cookieclicker.py [filename]")


cookie_clicker = CookieClicker()
cookie_clicker.run(sys.argv[1])
