#!/usr/bin/python3


def get_possible_cards():
    row = int(input())
    result = None
    for i in range(4):
        cards = set(map(int, input().split()))
        if i + 1 == row:
            result = cards
    return result

for test_case in range(int(input())):
    print('Case #{}: '.format(test_case + 1), end='')
    chosen = get_possible_cards().intersection(get_possible_cards())
    if not chosen:
        print('Volunteer cheated!')
    elif len(chosen) == 1:
        print(list(chosen)[0])
    else:
        print('Bad magician!')
