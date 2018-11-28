# -*- coding: utf-8 -*-

import sys


def solve():
    def get_cards():
        cards = []
        for _ in range(4):
            cards.append(list(map(int, input().split())))
        return cards

    r = [int(input()) - 1]
    card_sets = [get_cards()]
    r.append(int(input()) - 1)
    card_sets.append(get_cards())

    intersection = set(card_sets[0][r[0]]) & set(card_sets[1][r[1]])

    if len(intersection) > 1:
        return 'Bad magician!'
    elif len(intersection) < 1:
        return 'Volunteer cheated!'
    return intersection.pop()

def main():
    T = int(input())
    for i in range(T):
        print('Case #{}: {}'.format(i + 1, solve()))

if __name__ == '__main__':
    sys.exit(main())
