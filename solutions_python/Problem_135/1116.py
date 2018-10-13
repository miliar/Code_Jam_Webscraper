#!/usr/bin/env python3
# encoding: utf-8

if __name__ == '__main__':
    cases_n = int(input())
    for i in range(cases_n):
        # adjust to be 0 based
        row_volunteer = int(input())
        # read arrangemet
        for row in range(1, 1 + 4):
            tmp = input()
            if (row == row_volunteer):
                cards = set([int(j) for j in tmp.split()])
        row_volunteer = int(input())
        # read arrangemet
        for row in range(1, 1 + 4):
            tmp = input()
            if (row == row_volunteer):
                cards = cards.intersection([int(j) for j in tmp.split()])
        print('Case #{}: '.format(i + 1), end='')
        if len(cards) == 0:
            print('Volunteer cheated!')
        elif len(cards) == 1:
            print(list(cards)[0])
        else:
            print('Bad magician!')
