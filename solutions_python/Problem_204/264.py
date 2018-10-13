# -*- coding: utf-8 -*-
# !python3

__author__ = 'lostcoaster'

from trivial.codejam_thingy.files import Problem


class Packs(Problem):
    def __init__(self):
        super(Packs, self).__init__('B-small-attempt1')

    def solve(self, in_file):
        n, p = (int(x) for x in in_file.readline().strip().split(' '))
        recipe = [int(x) for x in in_file.readline().strip().split(' ')]
        packs = []
        for i in range(n):
            packs.append([int(x) for x in in_file.readline().strip().split(' ')])

        import math
        for i in range(n):
            for j in range(p):
                ser = (math.ceil(packs[i][j] / (1.1 * recipe[i])), math.floor(packs[i][j] / (0.9 * recipe[i])))
                if ser[1] < ser[0]:
                    ser = (0, 0)
                packs[i][j] = ser  # convert "gram" to "serve" range
            packs[i].sort(key=(lambda x: (x[1] - x[0], x[0])))  # sort from "least" range and "least start"

        c = 0
        while True:
            ret = None
            packs.sort(key=(lambda x: x[0][1] - x[0][0]))
            ser = packs[0].pop(0)
            if ser[0] != 0:
                ret = self._recusive_search_ing(packs, 1, ser[0], ser[1])
            if ret is not None:
                c += 1
                for i in range(1, n):
                    packs[i].remove(ret[i - 1])
            if any(len(x) == 0 for x in packs):
                break
        return c

    def _recusive_search_ing(self, packs, i, min_ser=None, max_ser=None):
        if i == len(packs):
            return []
        for cur in range(len(packs[i])):
            if packs[i][cur][0] == 0:
                continue  # invalid pack
            ret = None
            if min_ser is None:
                ret = self._recusive_search_ing(packs, i + 1, packs[i][cur][0], packs[i][cur][1])
            else:
                if max_ser >= packs[i][cur][0] and min_ser <= packs[i][cur][1]:
                    ret = self._recusive_search_ing(packs, i + 1, max(min_ser, packs[i][cur][0]),
                                                    min(max_ser, packs[i][cur][1]))
            if ret is not None:
                return [packs[i][cur]] + ret
        return None


if __name__ == '__main__':
    Packs().run()
