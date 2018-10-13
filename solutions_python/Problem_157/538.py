#!/usr/bin/env python3

from operator import mul
from functools import reduce

class Sign(object):
    def __mul__(self, other):
        if self.sgn == '+':
            return Sign(other.sgn)
        if other.sgn == '+':
            return Sign(self.sgn)
        return Sign('+')

    def __eq__(self, other):
        return self.sgn == other.sgn

    def __repr__(self):
        return '{}'.format(self.sgn)

    def __init__(self, sgn):
        self.sgn = sgn


class Quaternion(object):
    _table = { m: {n: v for n, v in zip('1ijk', l.split())}
                    for m, l in zip('1ijk', '''
                                    +1 +i +j +k
                                    +i -1 +k -j
                                    +j -k -1 +i
                                    +k +j -i -1'''.strip().split('\n')) }

    def __mul__(self, other):
        sgn, axe = self._table[self.axe][other.axe]
        return Quaternion(repr(Sign(self.sgn)*Sign(other.sgn)*Sign(sgn)) + axe)

    def __eq__(self, other):
        return self.sgn == other.sgn and self.axe == other.axe

    def __repr__(self):
        return '{}{}'.format(self.sgn, self.axe)

    def __init__(self, value):
        if len(value) == 1:
            value = '+' + value
        self.sgn = value[0]
        self.axe = value[1]


def prod(ls):
    return reduce(mul, ls)


def misspelling(ijks, x):
    sub_round = 1
    accumulate = Quaternion('+1')
    searching = [Quaternion(it) for it in 'kji']
    for run_round in range(x):
        if sub_round > 4:
            return False
        for c in ijks:
            accumulate *= Quaternion(c)
            if searching and searching[-1] == accumulate:
                sub_round = 0
                accumulate = Quaternion('+1')
                searching.pop()
        sub_round += 1
        if not searching:
            break
    if searching:
        return False
    round_product = prod([Quaternion(it) for it in ijks])
    rem_round = (x - run_round - 1) % 4
    accumulate = prod([accumulate] + [round_product] * rem_round)
    if accumulate == Quaternion('1'):
        return True


for case in range(int(input())):
    _, x = [int(n) for n in input().split()]
    ijks = input().strip()
    ans = 'YES' if misspelling(ijks, x) else 'NO'
    print('Case #{}: {}'.format(case+1, ans))
