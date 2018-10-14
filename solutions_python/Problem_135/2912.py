#!/usr/bin/env python

import sys


def guess_card(card_1, answer_1, card_2, answer_2):
    result = set(card_1[answer_1 - 1]).intersection(set(card_2[answer_2 - 1]))

    if len(result) == 1:
        return result.pop()
    elif len(result) == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'


def main():
    with open(sys.argv[1], 'r') as fi:
        n_round = int(fi.readline())

        r_round = 0
        while r_round < n_round:
            r_round += 1

            answer_1 = int(fi.readline())
            card_1 = []
            for i in range(4):
                card_1.append(map(int, fi.readline().split(' ')))

            answer_2 = int(fi.readline())
            card_2 = []
            for i in range(4):
                card_2.append(map(int, fi.readline().split(' ')))

            result = guess_card(card_1, answer_1, card_2, answer_2)
            print('Case #{0}: {1}'.format(r_round, result))


if __name__ == '__main__':
    main()
