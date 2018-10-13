# -*- coding: utf-8 -*-
import sys
from collections import OrderedDict

colors = None

class Impossible(Exception):
    pass


def solveNonPrimary(primary, other):
    G = colors.pop(other)

    if G == 0:
        return ""

    R = colors.pop(primary)

    if R < G + 1:
        if R == G and set(colors.values()) == {0}:
            string = "".join([primary,other]) * G
            colors[primary] = 0
        else:
            raise Impossible
    else:
        string = "".join([primary, other]) * G + primary
        colors[primary] = R-G-1

    return string


def solve(line):
    global colors
    N, R, O, Y, G, B, V = map(int,line.split())
    colors = dict(R=R, O=O, Y=Y, G=G, B=B, V=V)

    stringR = solveNonPrimary('R','G')
    stringB = solveNonPrimary('B','O')
    stringY = solveNonPrimary('Y','V')

    if max(map(len,[stringR,stringB,stringY])) == N:
        assert set(colors.values()) == {0}
        res = stringR + stringB + stringY
        if res[0] == res[-1]:
            raise Impossible
        else:
            return res

    strings = dict(
        R = ([stringR] if stringR else []) + ['R'] * colors['R'],
        B = ([stringB] if stringB else []) + ['B'] * colors['B'],
        Y = ([stringY] if stringY else []) + ['Y'] * colors['Y'],
    )


    result = ""

    while True:
        keys = sorted(strings.keys(), key=lambda k:
            (-len(strings[k]), 0 if k == result[:1] else 1))
        keys = filter(lambda k:len(strings[k]), keys)
        #print result, strings, keys

        if not keys:
            return result

        for c in keys:
            if result and result[-1] == c:
                continue
            try:
                result += strings[c].pop()
                break
            except IndexError:
                strings.pop(c)
        else:
            raise Impossible



if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        n_cases = int(f.readline())
        for i in xrange(n_cases):
            try:
                res = solve(f.readline())
                if res[0] == res[-1]:
                    raise Impossible
            except Impossible:
                res = 'IMPOSSIBLE'

            print 'Case #{}: {}'.format(i+1,res)