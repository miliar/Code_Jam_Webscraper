#!/usr/bin/env python3.4
import sys
import math

f = open('C-small-attempt0.in', 'r')
o = open('C0.out', 'w')

multiplication = {
    '1': {
        '1': (1, '1'),
        'i': (1, 'i'),
        'j': (1, 'j'),
        'k': (1, 'k')
    },
    'i': {
        '1': (1, 'i'),
        'i': (-1, '1'),
        'j': (1, 'k'),
        'k': (-1, 'j')
    },
    'j': {
        '1': (1, 'j'),
        'i': (-1, 'k'),
        'j': (-1, '1'),
        'k': (1, 'i')
    },
    'k': {
        '1': (1, 'k'),
        'i': (1, 'j'),
        'j': (-1, 'i'),
        'k': (-1, '1')
    }
}

def mult(tu, l):
    sign, sym = multiplication[tu[1]][l]
    return tu[0] * sign, sym

if __name__ == '__main__':
    for testCase in range(int(f.readline())):
        letterCount, repeat = map(int, f.readline().split())
        loop = f.readline()
        cur = (1, '1')
        cursor = 0
        while cursor < 4 * letterCount:
            cur = mult(cur, loop[cursor % letterCount])
            cursor += 1
            if cur[0] == 1 and cur[1] == 'i':
                break
        if 4 * letterCount == cursor:
            s = ('Case #%d: NO\n' % (testCase + 1))
        else:
            cur = (1, '1')
            while cursor < 8 * letterCount:
                cur = mult(cur, loop[cursor % letterCount])
                cursor += 1
                if cur[0] == 1 and cur[1] == 'j':
                    break
            if 8 * letterCount == cursor:
                s = ('Case #%d: NO\n' % (testCase + 1))
            else:
                cur = (1, '1')
                while cursor < 12 * letterCount:
                    cur = mult(cur, loop[cursor % letterCount])
                    cursor += 1
                    if cur[0] == 1 and cur[1] == 'k':
                        break
                if 12 * letterCount == cursor:
                    s = ('Case #%d: NO\n' % (testCase + 1))
                elif repeat <= (cursor - 1) // letterCount:
                    s = ('Case #%d: NO\n' % (testCase + 1))
                else:
                    cur = (1, '1')
                    remaining = (repeat - 1 - (cursor - 1) // letterCount) % 4
                    while cursor % letterCount != 0:
                        cur = mult(cur, loop[cursor % letterCount])
                        cursor += 1
                    for i in range(remaining * letterCount):
                        cur = mult(cur, loop[cursor % letterCount])
                        cursor += 1
                    if cur[0] == 1 and cur[1] == '1':
                        s = ('Case #%d: YES\n' % (testCase + 1))
                    else:
                        s = ('Case #%d: NO\n' % (testCase + 1))

        o.write(s)

