from __future__ import print_function
import math


class PC(object):
    def __init__(self, r, h):
        self.r = r
        self.h = h
        self.cr = 0

    def __gt__(self, other):
        return self.calc() > other.calc()

    def __repr__(self):
        return str((self.r, self.h))

    def calc_h(self):
        return 2 * self.r * math.pi * self.h

    def calc(self):
        if self.r > self.cr:
            return (self.r * self.r - self.cr * self.cr) * math.pi + self.calc_h()
        else:
            return self.calc_h()


class Template:
    def __init__(self):
        self.cout = True

    def process(self):
        ans = 0
        self.data = []
        self.pick = []
        self.N, self.K = [int(x) for x in self.fin.readline().strip().split()]
        for _ in range(self.N):
            r, h = [int(x) for x in self.fin.readline().strip().split()]
            self.data.append(PC(r, h))
#             self.print_tmp(str(PC(r, h)))
        max_r = 0
        for _ in range(self.K):
            self.data = sorted(self.data)
            p = self.data.pop()
            self.pick.append(p)
            max_r = p.r if p.r > max_r else max_r
            for x in self.data:
                x.cr = max_r
        for x in self.pick:
            ans += x.calc_h()
        ans += max_r * max_r * math.pi

        self.print_ans('%.9f' % ans)

    def solve(self):
        self.fin = open('../in.in', 'r')
        # self.fin = open('../test', 'r')
#         self.fin = open('../example.txt', 'r')
        self.fout = open('../out', 'w')
        times = int(self.fin.readline())
        for i in range(times):
            self.print_ans('Case #%d: ' % (i + 1))
            self.process()
            self.print_ans('\n')
        self.fin.close()
        self.fout.close()
        print('Done!')

    def make_test(self):
        fout = open('../test', 'w')
        fout.write('1\n2000\n')
        for i in range(2000):
            fout.write('%d %d\n' % ((-1000 + i), 1000 - i))
        fout.close()

    def print_tmp(self, s):
        if self.cout:
            print(str(s))

    def print_ans(self, s):
        self.fout.write(str(s))
        if self.cout:
            print(str(s), end='')


def nC2(n):
    return int(n * (n - 1) / 2)


def line(a, b):
    return pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)


if __name__ == '__main__':
    t = Template()
    t.solve()
