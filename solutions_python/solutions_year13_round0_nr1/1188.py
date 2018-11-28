#!/usr/bin/python3

from __future__ import print_function

from collections import defaultdict

class Board:
    possible_results = dict(
        X='X won',
        O='O won',
        draw='Draw',
        not_complete='Game has not completed'
    )

    def __init__(self, rows):
        self.rows = list()

        for r in range(4):
            row = [x for x in rows[r]]

            if len(row) != 4:
                raise RuntimeError('Row length != 4')

            self.rows.append(row)

        self.result = None

    def solve(self):
        X = 'X'
        O = 'O'
        T = 'T'
        empty = '.'

        has_empty_slots = False

        def add_symbol(symbols, symbol):
            symbols[symbol] += 1

            if symbol == T:
                symbols[X] += 1
                symbols[O] += 1

        def check_for_winner(symbols):
            for player in [X, O]:
                if symbols[player] == 4:
                    self.result = self.possible_results[player]

        # check rows
        for row in self.rows:
            symbols = defaultdict(int)

            for symbol in row:
                add_symbol(symbols, symbol)

                if symbol == empty:
                    has_empty_slots = True

            check_for_winner(symbols)

        if self.result:
            return self.result

        # check columns
        for c in range(4):
            symbols = defaultdict(int)

            for r in self.rows:
                add_symbol(symbols, r[c])

            check_for_winner(symbols)

        if self.result:
            return self.result

        # check diagonals
        symbols = defaultdict(int)
        for x in range(4):
            add_symbol(symbols, self.rows[x][x])
        check_for_winner(symbols)

        symbols = defaultdict(int)
        for x in range(4):
            add_symbol(symbols, self.rows[x][abs(x-3)])
        check_for_winner(symbols)

        if self.result == None:
            if has_empty_slots:
                self.result = self.possible_results['not_complete']
            else:
                self.result = self.possible_results['draw']

        return self.result

def main():
    no_test_cases = int(input())

    for i in range(1, no_test_cases + 1):
        rows = list()

        for _ in range(4):
            rows.append(input())

        if input() != '':
            raise RuntimeError('No empty line after test case %d' % i)

        board = Board(rows)
        board.solve()
        print('Case #{0}: {1}'.format(i, board.result))

if __name__ == '__main__':
    main()
