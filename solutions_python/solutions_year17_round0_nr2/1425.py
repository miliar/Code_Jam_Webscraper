#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-08 14:55:19

import logging
import argparse
from copy import deepcopy


def func(p, q):
    lp, lq = len(p), len(q)
    if lp < lq:
        return -1
    if lp > lq:
        return 1
    sp = ''.join(p)
    sq = ''.join(q)
    if sp < sq:
        return -1
    if sp > sq:
        return 1
    return 0


def work(args):
    lines = []
    with open(args.input) as fin:
        for el in fin:
            lines.append(el.strip())
    with open(args.output, 'w')as fout:
        C = int(lines[0])
        for case in range(1, C + 1):
            ss = list(lines[case])
            if ss[0] == '1':
                ans = ss[1:]
                for i in range(len(ans)):
                    ans[i] = '9'
            else:
                ans = deepcopy(ss)
                ans[0] = chr(ord(ss[0]) - 1)
                for i in range(1, len(ans)):
                    ans[i] = '9'
            # logging.info(ans)
            for i in range(len(ss)):
                temp = ss[:-i]
                if not i:
                    temp = ss[:]
                fail = False
                for j in range(1, len(temp)):
                    if temp[j] < temp[j - 1]:
                        fail = True
                if fail:
                    continue
                if i:
                    if ss[-i] == '0':
                        continue
                    if i == len(ss) and ss[-i] == '1':
                        continue
                    if temp and int(ss[-i]) - 1 < int(temp[-1]):
                        continue
                    temp.append(chr(ord(ss[-i]) - 1))
                    for j in range(1, i):
                        temp.append('9')
                if func(temp, ss) <= 0 and func(temp, ans) > 0:
                    ans = temp
                # logging.info('%d %s %s %s', i, ''.join(ans), ''.join(temp), ''.join(ss))
            fout.write('Case #%d: %s\n' % (case, ''.join(ans)))


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--input', '-i', help='input file', required=True)
    argparser.add_argument('--output', '-o', help='output file', required=True)
    args = argparser.parse_args()
    work(args)


if __name__ == '__main__':
    logging.root.setLevel(logging.INFO)
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)s[%(asctime)s %(filename)s:%(lineno)d]%(message)s')
    main()
