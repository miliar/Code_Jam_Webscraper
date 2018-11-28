#!/usr/bin/env python

import sys
import os

def get_line(lines):
    line = int(lines.pop(0))
    cards = [[int(i) for i in l.split(' ')] for l in lines[0:4]]

    return (cards[line-1], lines[4:])

def main():
    lines = sys.stdin.readlines()
    test_num = int(lines.pop(0))

    for i in range(test_num):
        cards1, lines = get_line(lines)
        cs1 = set(cards1)

        cards2, lines = get_line(lines)
        cs2 = set(cards2)

        ans = (cs1 & cs2)
        if len(ans) == 1:
            print("Case #%d: %d" % (i+1, list(ans)[0]))
        elif len(ans) > 1:
            print("Case #%d: Bad magician!" % (i+1))
        else:
            print("Case #%d: Volunteer cheated!" % (i+1))

if __name__ == '__main__':
    main()


