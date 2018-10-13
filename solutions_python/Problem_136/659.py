#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CookieGame(object):
    def __init__(self, C, F, X):
        self.C = C
        self.F = F
        self.X = X
        self.asset = 0.0
        self.farm = 0
        self.elapsed_time = 0.0

    def p(self):
        print 'C: ', self.C
        print 'F: ', self.F
        print 'X: ', self.X

    def speed(self):
        return 2.0 + self.F * self.farm

    def win_buy_next_farm(self):
        buy_farm_time = (self.C - self.asset) / self.speed()
        need_time = self.X / (self.speed() + self.F)
        return buy_farm_time + need_time

    def win_not_buy_next_farm(self):
        to_gain = self.X - self.asset
        need_time = to_gain / self.speed()
        return need_time

    def should_buy_farm(self):
        if self.win_buy_next_farm() < self.win_not_buy_next_farm():
            return True
        else:
            return False

    def buy_farm(self):
        to_gain = self.C - self.asset
        used_time = to_gain / self.speed()
        self.elapsed_time += used_time
        self.farm += 1
        self.asset = 0.0
        return None

    def wait_until_win(self):
        to_gain = self.X - self.asset
        self.elapsed_time += to_gain / self.speed()
        return None

    def run(self, f_out, i):
        while self.should_buy_farm():
            self.buy_farm()
        self.wait_until_win()
        # print '%.7f' % self.elapsed_time
        f_out.write('Case #%d: %.7f\n' % (i, self.elapsed_time))


def read_input(in_path, out_path):
    f_in = open(in_path)
    f_out = open(out_path, 'wb')
    T = int(f_in.readline().strip())
    print T
    for i in range(T):
        line = f_in.readline().strip()
        C, F, X = [float(e) for e in line.split()]
        cg = CookieGame(C, F, X)
        # cg.p()
        cg.run(f_out, i + 1)
    f_in.close()
    f_out.close()


def main():
    # read_input('sample.in', 'sample.out')
    # read_input('small.in', 'small.out')
    read_input('large.in', 'large.out')





if __name__ == '__main__':
    main()