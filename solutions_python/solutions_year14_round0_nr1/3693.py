#!/usr/bin/env python
import sys


class Case(object):

    def __init__(self, first_guess, first_board, second_guess, second_board):
        self.first_guess = first_guess
        self.first_board = first_board
        self.second_guess = second_guess
        self.second_board = second_board

    def find_card(self):
        possible_numbers = set(self.first_board[self.first_guess - 1])
        second_numbers = set(self.second_board[self.second_guess - 1])
        results = possible_numbers.intersection(second_numbers)
        if len(results) > 1:
            return "Bad magician!"
        elif len(results) < 1:
            return "Volunteer cheated!"
        else:
            return str(list(results)[0])

def parse_file(file_name):
    with open(file_name) as f:
        lines = [line.strip() for line in f.readlines()]
        num_test_cases = int(lines.pop(0))

        cases = []
        for i in range(num_test_cases):
            first_guess = int(lines.pop(0))
            first_board = [[int(l) for l in lines.pop(0).split(" ")] for j in range(4)]

            second_guess = int(lines.pop(0))
            second_board = [[int(l) for l in lines.pop(0).split(" ")] for j in range(4)]

            cases.append(Case(first_guess, first_board, second_guess, second_board))
        return cases


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        cases = parse_file(sys.argv[1])
        for idx, case in enumerate(cases):
            print "Case #" + str(idx + 1) + ": " + case.find_card()
