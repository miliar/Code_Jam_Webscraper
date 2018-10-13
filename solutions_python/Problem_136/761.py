# -*- coding: utf-8 -*-
# This library is available online and free to use:
# https://github.com/yanatan16/pycodejam
from codejam.parsers import iter_parser


def solve(*lines):
    # print lines
    C, F, X = lines
    rate = 2
    memo = [0]
    time = X / rate
    while 1:
        memo.append(C / rate + memo[-1])
        new_rate = rate + F
        new_time = memo[-1] + X / new_rate
        if new_time > time:
            return '{:0.7f}'.format(time)
        rate = new_rate
        time = new_time


@iter_parser
def parse(nxtline):
    return map(float, nxtline().split())


if __name__ == "__main__":
    from codejam import CodeJam
    CodeJam(parse, solve).main()
