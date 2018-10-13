#!/usr/bin/env pypy

import sys


def read(lines):
    h, w = lines[0].split()
    w = int(w)
    h = int(h)
    case = [['?'] * (w + 2)]
    for y in range(h):
        case.append(['?'] + list(lines[1 + y]) + ['?'])
    case.append(['?'] * (w + 2))
    return case, lines[1 + y + 1:]


def go(case):
    for xd, yd in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        #print '\n' + '\n'.join(''.join(l) for l in case) ###

        for m in range(1, max(len(case) - 1, len(case[0]) - 1)):
            for y in range(1, len(case) - 1):
                for x in range(1, len(case[0]) - 1):
                    if case[y][x] != '?':
                        continue
                    case[y][x] = case[y + yd][x + xd]

    #while True:
        #f = False
        #for y in range(1, len(case) - 1):
        #    for x in range(1, len(case[0]) - 1):
        #        c = case[y][x]
        #        if c != '?':
        #            continue
        #        f = True

        #        #xn = case[y][x - 1]
        #        #xp = case[y][x + 1]
        #        #yn = case[y - 1][x]
        #        #yp = case[y + 1][x]

        #        print 'trying',x,y
        #        for xd, yd in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        #            p = case[y + yd][x + xd]
        #            if p == '?':
        #                continue
        #            print 'potential',p,'at',xd,yd
        #            for xd2, yd2 in [(a, b) for a in range(-1, 1 + 1) for b in range(-1, 1 + 1)]:
        #                print xd2,yd2
        #                if not xd2 and not yd2:
        #                    continue
        #                if (xd2 == xd and not yd2) or (yd2 == yd and not xd2):
        #                    continue
        #                print 'checking', xd2,yd2,x+xd2,y+yd2,case[y+yd2][x+xd2]
        #                if case[y + yd2][x + xd2] == p:
        #                    print 'oops hit at',xd2,yd2
        #                    break
        #            else:
        #                case[y][x] = p
        #                break

        #        #o = '?'
        #        #if xn != '?' and yn != xn and yp != xn:
        #        #    o = xn
        #        #elif xp != '?' and yn != xp and yp != xp:
        #        #    o = xp
        #        #elif yn != '?' and xn != yn and xp != yn:
        #        #    o = yn
        #        #elif yp != '?' and xn != yp and xp != yp:
        #        #    o = yp

        #        #case[y][x] = o


        #if not f:
        #    break

    return '\n' + '\n'.join(''.join(l[1:-1]) for l in case[1:-1])


def main():
    lines = sys.stdin.read().splitlines()

    cases = int(lines[0])
    lines = lines[1:]

    for i in range(cases):
        assert lines
        case, lines = read(lines)
        print 'Case #%d:%s' % (i + 1, go(case))

    assert not lines


if __name__ == '__main__':
    main()
