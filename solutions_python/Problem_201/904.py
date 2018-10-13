#!python3
# -*- coding: utf-8 -*-

__author__ = 'lostcoaster'

import trivial.codejam_thingy.files as f


class Stalls(f.Problem):
    def __init__(self):
        super(Stalls, self).__init__('C-small-2-attempt0')

    def solve(self, fin):
        n, k = (int(x) for x in fin.readline().strip().split(' '))
        width = 1
        while 2 * width - 1 < k:
            width *= 2
        remain = k - (width - 1)  # not full layer
        vac = n - (width - 1)
        skip = vac // width
        if remain <= vac % width:
            skip += 1
        if skip % 2 == 1:
            return f'{skip//2:.0f} {skip//2:.0f}'
        else:
            return f'{skip//2:.0f} {skip//2 - 1:.0f}'


if __name__ == '__main__':
    Stalls().run()

if __name__ == '__main__':
    Stalls().run()
