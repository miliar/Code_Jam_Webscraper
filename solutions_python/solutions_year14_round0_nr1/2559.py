#!/usr/bin/python
import fileinput


def get_input():
    input = [line.strip() for line in fileinput.input()]

    # split the input up into number of cases and cardsets
    num_cases = input.pop(0)
    _cases = [input[i:i + 10] for i in range(0, len(input), 10)]

    cases = list()
    for case in _cases:
        _temp = list()
        for i in xrange(0, len(case), 5):
            _temp.append(case[i:i + 5])
        cases.append(_temp)
    cases.append(num_cases)

    return cases


def solve_trick(card_set):
    rows = list()
    for cards in card_set:
        row_num = int(cards.pop(0)) - 1
        row = [int(i) for i in cards[row_num].split()]
        rows.append(row)

    card = list(set(rows[0]).intersection(set(rows[1])))

    if not card:
        return "Volunteer cheated!"
    if len(card) == 1:
        return str(card[0])
    if len(card) > 1:
        return "Bad magician!"


def main():
    input = get_input()
    num_cases = input.pop()

    for case_num, card_set in enumerate(input, 1):
        print 'Case #{num}: {result}'.format(num=case_num, result=solve_trick(card_set))


if __name__ == '__main__':
    main()
