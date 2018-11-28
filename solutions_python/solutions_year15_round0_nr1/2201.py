#!/usr/bin/env python
from __future__ import print_function
from collections import defaultdict
import sys


def read_int():
    return int(raw_input())


def read_int_ls():
    return [int(x) for x in raw_input().split()]


def read_ls():
    return [int(x) for x in raw_input().split()]


def convert_ppl_list_to_dict(xs):
    ppl = defaultdict(int)

    for i, x in enumerate(xs):
        ppl[i] = x

    return ppl


def run(shy_max, ppl):
    standing = ppl[0]
    friends = 0

    for shy_level in xrange(1, shy_max + 1):
        shy_ppl = ppl[shy_level]
        friends += max(0, shy_level - (standing + friends))
        standing += shy_ppl

    return friends


def main():
    for i in range(read_int()):
        # input data
        data = raw_input().split()
        ppl_cnt = int(data[0])
        ppl = convert_ppl_list_to_dict(map(int, list(data[1])))
        # print(ppl)

        # evaluate
        result = run(ppl_cnt, ppl)

        # output
        print("Case #%d: %s" % (i + 1, result))

if __name__ == "__main__":
    #profile.run('main()')
    sys.exit(main())
