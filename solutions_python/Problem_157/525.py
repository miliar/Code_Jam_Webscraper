__author__ = 'alex'

import gc
from copy import copy

indices = {'1': 0,
           'i': 1,
           'j': 2,
           'k': 3}


class ShitNumber:
    sign = 1
    letter = ''

    def __init__(self, letter, sign=1):
        self.letter = letter
        self.sign = sign

    def __str__(self):
        return self.letter if self.sign == 1 else '-'+self.letter

    def __repr__(self):
        return str(self)

    def swap_sign(self):
        self.sign = -self.sign

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__


table = [
    [ShitNumber('1'), ShitNumber('i'), ShitNumber('j'), ShitNumber('k')],
    [ShitNumber('i'), ShitNumber('1', -1), ShitNumber('k'), ShitNumber('j', -1)],
    [ShitNumber('j'), ShitNumber('k', -1), ShitNumber('1', -1), ShitNumber('i')],
    [ShitNumber('k'), ShitNumber('j'), ShitNumber('i', -1), ShitNumber('1', -1)]
]


def prod(sn1, sn2):
    if sn1.sign == -1:
        if sn2.sign == -1:
            sn2.swap_sign()
            sn1.swap_sign()
            ret = copy(table[indices[sn1.letter]][indices[sn2.letter]])
            return ret
        else:
            sn1.swap_sign()
            ret = copy(table[indices[sn1.letter]][indices[sn2.letter]])
            ret.swap_sign()
            return ret
    if sn2.sign == -1:
        if sn1.sign == 1:
            sn2.swap_sign()
            ret = copy(table[indices[sn1.letter]][indices[sn2.letter]])
            ret.swap_sign()
            return ret
    if sn1.sign == 1 and sn2.sign == 1:
        return copy(table[indices[sn1.letter]][indices[sn2.letter]])

# print(prod(ShitNumber('k', -1), ShitNumber('j')))


def test(f):
    L, X = f.readline().strip().split()
    X = int(X)
    if X > 12: X = 12 + X % 4
    string = f.readline().strip()
    ans = ''

    w = []
    for i in range(0, X):
        for l in string:
            w.append(ShitNumber(l, 1))

    letters = [ShitNumber('i'), ShitNumber('j')]
    status = []

    i = 0
    ii = 0

    while (len(w) > 1) and (ii < 2):
        # print(w)
        if w[0] == letters[ii]:
            status.append(w[0])
            ii += 1
            del w[0]
        else:
            w[0] = prod(w[0], w[1])
            del w[1]

    # print(status)

    if len(status) == 2:
        for iii in w:
            status.append(iii)

        while len(status) > 1:
            status[0] = prod(status[0], status[1])
            del status[1]

        ans = 'YES'
        if not (str(status[0]) == '-1'):
            ans = 'NO'
    else:
        ans = 'NO'

    print('Case #'+str(tests+1)+': '+ans)
    gc.collect()


f = open('input', 'r')
T = f.readline().rstrip('\n')

for tests in range(0, int(T)):
    test(f)

f.close()