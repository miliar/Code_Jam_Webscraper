# -*- coding: utf-8 -*-
__author__ = 'AlexWMF'

import sys
import os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'A-small-attempt0.in'))
sys.stdout = open('out1.txt', 'wb')


def main():
    cases = int(raw_input())

    #table = list(list([0, 0, 0, 0]) for i in range(4))

    for case in range(cases):
        first_line = int(raw_input()) - 1

        line = None

        for l in range(4):
            if first_line != l:
                raw_input()
            else:
                line = [int(x) for x in raw_input().split(' ')]

        second_line = int(raw_input()) - 1

        line2 = []
        for l in range(4):
            if second_line != l:
                raw_input()
            else:
                line2 = [int(x) for x in raw_input().split(' ')]

        diff = set.intersection(*[set(line), set(line2)])
        case_num = case + 1

        if len(diff) == 1:
            print 'Case #%s: %u' % (case_num, diff.pop())
        elif not len(diff):
            print 'Case #%s: Volunteer cheated!' % (case_num,)
        else:
            print 'Case #%s: Bad magician!' % (case_num,)




if __name__ == '__main__':
    main()