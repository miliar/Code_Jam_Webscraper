#!/usr/bin/env python3

def read_cards():
    cards = [input().strip().split() for _ in range(4)]
    return cards
        

T = int(input())
for i in range(1, T + 1):
    ans1 = int(input())
    cards1 = read_cards()
    ans2 = int(input())
    cards2 = read_cards()
    s = set(cards1[ans1 - 1]) & set(cards2[ans2 - 1])
    if len(s) == 1:
        res = s.pop()
    elif len(s) == 0:
        res = 'Volunteer cheated!'
    else:
        res = 'Bad magician!'
    print('Case #{0}: {1}'.format(i, res))
