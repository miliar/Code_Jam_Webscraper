#!python3
# -*- coding: utf-8 -*-

__author__ = 'lostcoaster'

import trivial.codejam_thingy.files as f

class Tidy(f.Problem):
    def __init__(self):
        super(Tidy, self).__init__('B-large')

    def solve(self, fin):
        num = fin.readline().strip()
        num = [int(n) for n in num]
        for i in range(1, len(num)):
            for j in range(1, len(num)):
                if num[j] < num[j - 1]:
                    num[j - 1] -= 1
                    num[j] += 10
        num = ''.join(str(min(9, i)) for i in num)
        num = num.lstrip('0')
        return num

if __name__ == '__main__':
    Tidy().run()


