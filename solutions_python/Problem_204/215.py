import sys
from collections import Counter
import itertools
import numpy as np


def get_line(format, line=None, extract_if_one=True):
    line = next(sys.stdin) if line is None else line
    types = {
        'i': int,
        'f': float,
        's': str,
    }
    line = line.strip().split(' ')
    assert len(line) == len(format)
    for i, t in enumerate(format):
        line[i] = types[t](line[i])
    return tuple(line) if len(line) > 1 or not extract_if_one else line[0]

class Problem:
    # def amount_to_serving(self, amount, require):
    #     serving = round(float(amount)/require)
    #     if amount < 0.9 * serving * require or amount > 1.1 * serving * require:
    #         serving = 0
    #     return serving
    def amount_to_serving(self, amount, require):
        valid = []
        for i in range(int(amount/(0.9*require)), int(amount/(1.1*require))-1, -1):
            if float(i)*0.9*require <= amount and float(i)*1.1*require >= amount:
                valid.append(i)
                break
        for i in range(int(amount/(1.1*require)), int(amount/(0.9*require))+1, +1):
            if float(i)*0.9*require <= amount and float(i)*1.1*require >= amount:
                valid.append(i)
                break
        if len(valid) == 0:
            valid = [0]
        # print ('a2s', amount, require, (min(valid), max(valid)))
        return (min(valid), max(valid))




    def __init__(self):
        n, p = get_line('ii')
        self.n = n
        self.p = p
        self.require = get_line('i'*n, extract_if_one=False)
        self.packages = []
        self.ans = 0
        # print('req', self.require)
        flag = False
        for i in range(n):
            amounts = get_line('i'*p, extract_if_one=False)
            f = lambda x: self.amount_to_serving(x, self.require[i])
            pack = list(map(f, amounts))
            # print()
            # print('amo', i, amounts)
            # print('pck', i, pack)
            # print('pck sort', i, sorted(pack))
            pack = sorted(pack)
            while len(pack) > 0 and pack[0][1] == 0:
                del pack[0]
            if len(pack) == 0:
                flag = True
            self.packages.append(pack)
        if flag:
            return

        while True:
            # print(self.packages)
            # find maximum min a
            maxmin = 0
            for i in range(n):
                if len(self.packages[i]) == 0:
                    return
                # print(maxmin, self.packages[i][0])
                maxmin = max(maxmin, self.packages[i][0][0])
            # del all that max < a
            for i in range(n):
                while len(self.packages[i]) > 0 and self.packages[i][0][1] < maxmin:
                    del self.packages[i][0]
                # print(len(self.packages[i]), 'shit', self.packages[i])
                if len(self.packages[i]) == 0:
                    return
            self.ans += 1
            # print('ans')
            for i in range(n):
                del self.packages[i][0]

    def solve(self):
        print(self.ans)


def main():

    sys.stdin = open('B-small-attempt0.in', 'r')
    sys.stdout = open('b.out', 'w')
    T = get_line('i')
    for i in range(T):
        print('Case #%d: ' % (i+1, ), end='')
        p = Problem()
        p.solve()


if __name__ == '__main__':
    main()
