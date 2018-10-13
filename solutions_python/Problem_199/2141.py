#!/usr/bin/python
import io

T = int(raw_input())
ret = 'IMPOSSIBLE'

def flip(p, c, flipper):
    ret = []
    for xx in range(len(p)):
        if xx >= c and xx <= (c + (flipper - 1)):
            if p[xx] == '-':
                ret.append('+')
            else:
                ret.append('-')
        else:
            ret.append(p[xx])
    return ''.join(ret)

for current_T in range(1, T + 1):
    steps = 0
    pancakes = raw_input()
    pancakes, flipper = pancakes.split(' ')
    flipper = int(flipper)

    if '-' not in pancakes:
        print 'Case #%d: 0' % current_T
        continue

    s = len(pancakes)
    cursor = 0
    while True:
        if pancakes[cursor] == '-':
            pancakes = flip(pancakes, cursor, flipper)
            steps += 1

        if cursor == (s - flipper):
            if '-' not in pancakes:
                print 'Case #%d: %d' % (current_T, steps)
            else:
                print 'Case #%d: IMPOSSIBLE' % current_T
            break

        cursor += 1
