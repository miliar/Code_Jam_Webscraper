#!/usr/bin/env python

import sys

stdin = sys.stdin

msg = {
    'magicianfail': 'Bad magician!',
    'volunteerfail': 'Volunteer cheated!',
    }

class Err(Exception):
    pass


def read_cards(f):
    r = []
    for _ in range(4):
        row = f.readline().strip().split(' ')
        if len(row) != 4:
            raise Err('4 cards expected')
        row = map(int, row)
        r.append(row)
    return r

def sanity_check(cards):
    A = cards
    cards_list = []

    for _row in A:
        cards_list.extend(_row)

    cards_set = set(cards_list)
    if len(cards_set) < len(cards_list):
        raise Err('redundant cards?')


n = int(stdin.readline().strip())

for i in range(n):
    x = i + 1

    a1 = int(stdin.readline().strip())
    A1 = read_cards(stdin)
    a2 = int(stdin.readline().strip())
    A2 = read_cards(stdin)

    sanity_check(A1)
    sanity_check(A2)

    row1 = A1[a1-1]
    row2 = A2[a2-1]

    row1and2 = list(set(row1).intersection(set(row2)))

    if len(row1and2) == 1:
        r = row1and2[0]
    elif len(row1and2) > 1:
        r = msg['magicianfail']
    elif len(row1and2) == 0:
        r = msg['volunteerfail']

    print 'Case #%i: %s' % (x, r)





