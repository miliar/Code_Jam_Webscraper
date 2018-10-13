#!/usr/bin/env python
import fileinput


class CookieGame(object):
    def __init__(self, C, F, X):
        self.C = C  # farm cost
        self.F = F  # farm power
        self.X = X  # goal

        self.f = 2.  # current power
        self.t = 0.  # clock
        self.x = 0.  # current cookies count

    def time_until_next_farm(self):
        need = self.C - self.x
        if need <= 0:
            return 0
        return need / self.f

    def time_until_win(self):  # without buying anything
        need = self.X - self.x
        if need <= 0:
            return 0
        return need / self.f

    def time_until_win_with_another_farm(self):
        time_until_can_buy = self.time_until_next_farm()
        # *at that point* how much will we need?
        need = self.X - self.x + self.C - self.f * time_until_can_buy
        time_until_win = need / (self.f + self.F)
        return time_until_can_buy + time_until_win

    def better_to_wait(self):
        return self.time_until_win_with_another_farm() <= self.time_until_win()

    def time_needed_for_goal(self):
        while self.better_to_wait():
            self.buy_farm()
        self.go_later(self.time_until_win())
        return self.t

    def buy_farm(self):
        self.go_later(self.time_until_next_farm())
        self.x -= self.C
        self.f += self.F

    def go_later(self, seconds):
        self.t += seconds
        self.x += self.f * seconds


def solve_round(C, F, X):
    return CookieGame(C, F, X).time_needed_for_goal()


def make_answer(case, result):
    return "Case #%s: %.7f" % (case, result)


def get_input(lines):
    nextline = lambda: next(lines)
    cases = int(nextline())
    for _ in range(cases):
        yield map(float, nextline().split())


def main():
    for i, game in enumerate(get_input(fileinput.input()), 1):
        print(make_answer(i, solve_round(*game)))

if __name__ == '__main__':
    main()
