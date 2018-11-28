#!/usr/bin/env python
# -*- mode:python; coding:utf-8; indent-tabs-mode:nil -*-
#
# Problem A. Swinging Wild
# http://code.google.com/codejam/contest/1842485/dashboard#s=p0
#

import sys
import itertools


class Vine:
    def __init__(self, pos, length):
        self.pos = pos
        self.length = length

    def __str__(self):
        return 'Vine(%d,%d)' % (self.pos, self.length)


def solve(D, vines):
    #print D, ' '.join(map(str, vines))
    q = [(0, 0)]
    while q:
        # pos の場所にいて vine をつかんでいる(つるの長さは length)
        pos, index = q.pop()
        vine = vines[index]
        length = min(vine.pos - pos, vine.length)
        #print pos, vine, length

        if vine.pos + length >= D:
            return 'YES'

        for index in range(index + 1, len(vines)):
            delta = vines[index].pos - vine.pos
            if delta <= length:
                # このつるもつかめる
                if delta < vines[index].length:
                    q.append((vine.pos, index))
                else:
                    # 揺れながらつるを登る
                    q.append((vines[index].pos - vines[index].length, index))

    return 'NO'


def main(INPUT, OUTPUT):
    T = int(INPUT.readline())
    for index in range(T):
        # 進捗表示
        sys.stderr.write('#%d\r' % (index + 1))
        N = int(INPUT.readline())
        vines = [Vine(*map(int, INPUT.readline().split())) for i in range(N)]
        D = int(INPUT.readline())
        OUTPUT.write('Case #%d: %s\n' % (index + 1, solve(D, vines)))


def makesample(Nmax, T=30):
    import random
    print T
    for index in range(T):
        N = random.randint(1, Nmax)
        D = random.randint(N, 10**9)
        print N
        d = 0
        for i in range(N):
            d = random.randint(d + 1, D - (N - i))
            l = random.randint(d if i == 0 else 1, 10**9)
            print d, l
        print D


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if ('-makesample', 'small') == tuple(sys.argv[1:]):
            makesample(100)
        elif ('-makesample', 'large') == tuple(sys.argv[1:]):
            makesample(10000)
        else:
            print 'usage: %s [-makesample <small|large>]' % sys.argv[0]
    else:
        main(sys.stdin, sys.stdout)

