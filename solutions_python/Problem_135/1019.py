#!/usr/bin/python
# -*- coding: utf-8 -*-


def solve(ans_1, board_1, ans_2, board_2):

    # print ans_1
    # print board_1
    # print ans_2
    # print board_2

    row_1 = board_1[ans_1-1]
    row_2 = board_2[ans_2-1]

    set_row_1 = set(row_1)
    set_row_2 = set(row_2)

    intersection = set_row_1 & set_row_2
    if intersection:
        # 2 possible cases, either correct anser or bad magician
        if len(intersection) == 1:
            return next(iter(intersection))
        else:
            return 'Bad magician!'
    else:
        # volunteer cheated
        return 'Volunteer cheated!'

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):

        ans_1 = input()
        board_1 = []
        for i in range(4):
            row = raw_input()
            row_items = row.strip().split()
            row = [int(item) for item in row_items]
            board_1.append(row)

        ans_2 = input()
        board_2 = []
        for i in range(4):
            row = raw_input()
            row_items = row.strip().split()
            row = [int(item) for item in row_items]
            board_2.append(row)

        # print cipher
        print("Case #%i: %s" % (caseNr, solve(ans_1, board_1, ans_2, board_2)))
