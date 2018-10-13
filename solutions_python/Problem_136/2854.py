#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class CookieProblem(object):

    def __init__(self):
        with open('input.txt', 'r') as f:
            self.lines = f.readlines()
            self.nb_test_case = int(self.lines[0])

    def solver(self):
        for counter, line in enumerate(self.lines):
            print counter
            if counter == 0:
                continue
            values = line.split()
            cost = float(values[0])
            cookie_second_farm = float(values[1])
            goal = float(values[2])
            self.nb_cookie = 0
            self.cookie_sec = 2
            self.time = 0
            self.cond = True
            while self.cond:
                ans = self.solve(cost,
                                 cookie_second_farm, goal)
            self.answer(counter, ans)

    def solve(self, cost, cookie_second_farm, goal):
        wait_and_see_time = (goal - self.nb_cookie) / self.cookie_sec
        while self.nb_cookie > cost:
            self.nb_cookie -= cost
            self.cookie_sec += cookie_second_farm
            wait_and_see_time_2 = (goal - self.nb_cookie) / self.cookie_sec
            if wait_and_see_time_2 > wait_and_see_time:
                self.nb_cookie += cost
                self.cookie_sec -= cookie_second_farm
                break
            else:
                wait_and_see_time = wait_and_see_time_2

        buy_farm_time = (cost - self.nb_cookie) / self.cookie_sec
        self.cookie_sec += cookie_second_farm
        new_wait_and_see = ((goal - self.nb_cookie) / self.cookie_sec) + buy_farm_time
        if new_wait_and_see > wait_and_see_time:
            self.cond = False
            return (self.time + wait_and_see_time)
        else:
            self.time += buy_farm_time
            # return self.solve(nb_cookie, cookie_sec, cost,
                              # cookie_second_farm, goal, time + buy_farm_time)

    def answer(self, counter, ans):
        with open('output.txt', 'a') as output:

                case = "Case #" + str(counter) + ': '
                return_carriage = '\n'
                output.write(case + "{:.7f}".format(ans) + return_carriage)


if __name__ == '__main__':
    A = CookieProblem()
    A.solver()
