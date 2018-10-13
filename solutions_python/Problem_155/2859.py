# -*- coding: utf-8 -*-
# This library is available online and free to use:
# https://github.com/yanatan16/pycodejam
from codejam.parsers import iter_parser


def solve(*lines):
    S_max, persons = lines
    sum = 0
    additional_guests = 0
    for i in xrange(len(persons)):
        if i > sum:
            additional_guests += i - sum
            sum += i - sum
        sum += persons[i]
    return additional_guests

@iter_parser
def parse(nxtline):
    S_max, _, persons = nxtline().partition(' ')
    return S_max, map(int, persons)

if __name__ == "__main__":
    from codejam import CodeJam
    CodeJam(parse, solve).main()
