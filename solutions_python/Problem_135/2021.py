#!/usr/bin/env python3
import sys


def process_input(filename):
    with open(filename) as f:
        f.readline()

        answer, board = None, []
        while True:
            line = f.readline()
            if not line:
                break

            if answer is None:
                answer = int(line.strip())
            elif len(board) < 4:
                board.append(tuple(int(n) for n in line.split()))
            else:
                yield answer, board
                answer, board = int(line.strip()), []

        yield answer, board


def solve(situation1, situation2):
    answer1, board1 = situation1
    answer2, board2 = situation2

    possible_cards = set(board1[answer1-1])
    selected_card = possible_cards & set(board2[answer2-1])

    if len(selected_card) == 1:
        return str(selected_card.pop())
    elif len(selected_card) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print('Missing filename', file=sys.stderr)
        sys.exit(1)

    input_gen = process_input(filename)

    num_case = 1
    while True:
        try:
            situation1, situation2 = next(input_gen), next(input_gen)
        except StopIteration:
            break

        print("Case #{}: {}".format(num_case, solve(situation1, situation2)))
        num_case += 1
