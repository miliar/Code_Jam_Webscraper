# -*- coding: utf-8 -*-

from base import CodeJamBase
import sys

__author__ = "Evan"

class CookieClicker(CodeJamBase):

    def _collect_args(self):
        args = self._read_line_as_list()
        self.C = float(args[0])
        self.F = float(args[1])
        self.X = float(args[2])

        self.last_time = 1000000000
        self.time_for_n_farms = []

    def _test(self):
        
        n = 0
        while(True):
            new_time = self._time_for_n_farms(n)
            if new_time > self.last_time:
                break
            else:
                self.last_time = new_time
            n += 1

        return [str(round(self.last_time, 7))]

    def _time_for_n_farms(self, n):
        """
        compute the time it would take to reach the goal with n farms
        """
        res = 0
        for i in range(n):
            if len(self.time_for_n_farms) > i:
                term = self.time_for_n_farms[i]
            else:
                term = (self.C) / (2+(self.F * i))
                self.time_for_n_farms.append(term)
            res += term
        res += self.X / (2+(self.F * n))
        return res

def main():
    """
    copy this into any actual challenge solcing code
    """
    sim = CookieClicker()
    sim.run_tests(sys.argv[1])

if __name__ == "__main__":
    main()