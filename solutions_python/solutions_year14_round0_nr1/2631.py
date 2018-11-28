#!/usr/bin/python2
# -*- coding: utf8 -*-
# Google Code Jam 2014 - Qualification Round - Problem A - Mateusz Kurek


def get_board_row():
    volunteer_row = int(raw_input())
    for i in xrange(1, 5):
        row = raw_input()
        if volunteer_row == i:
            row1_numbers = set(row.split(' '))
    return row1_numbers


def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        row1, row2 = get_board_row(), get_board_row()
        common = row1.intersection(row2)
        if len(common) == 1:
            result = common.pop()
        elif len(common) == 0:
            result = 'Volunteer cheated!'
        else:
            result = 'Bad magician!'
        print('Case #{}: {}'.format(i, result))


if __name__ == '__main__':
    main()
