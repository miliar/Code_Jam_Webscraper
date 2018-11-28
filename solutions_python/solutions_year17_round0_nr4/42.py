import numpy as np
import sys

import codejam

DOT = 0
PLUS = 1
CROSS = 2
BOTH = 3


def parse_symbol(symbol):
    if symbol == '.':
        return DOT
    if symbol == '+':
        return PLUS
    if symbol == 'x':
        return CROSS
    if symbol == 'o':
        return BOTH


def encode_model(model):
    if model == DOT:
        return '.'
    if model == PLUS:
        return '+'
    if model == CROSS:
        return 'x'
    if model == BOTH:
        return 'o'


def place_cross(board):
    rows_without_cross = [row for row in range(0, board.shape[0])
                          if all(cell & CROSS == 0 for cell in board[row])]
    cols_without_cross = [col for col in range(0, board.shape[1])
                          if all(cell & CROSS == 0 for cell in board[:, col])]
    assert len(rows_without_cross) == len(cols_without_cross)
    for row, col in zip(rows_without_cross, cols_without_cross):
        board[row, col] |= CROSS


def bipartite_match(group_a, neighbors):
    matches = {}
    inv_matches = {}

    def try_match(a: int) -> bool:
        if a in visited:
            return False  # prevent infinite loop
        visited.add(a)
        for b in neighbors(a):
            if b not in inv_matches or try_match(inv_matches[b]):
                matches[a] = b
                inv_matches[b] = a
                return True
        return False

    for a in group_a:
        visited = set()
        try_match(a)

    return matches


def place_plus(board):
    """
    Find bipartite matching between
        Group A: i+j for (i, j) in cell
        Group B: i-j for (i, j) in cell
    """
    x, y = board.shape

    init_a = set()
    init_b = set()
    for i in range(0, x):
        for j in range(0, y):
            if board[i, j] & PLUS != 0:
                init_a.add(i+j)
                init_b.add(i-j)

    def neighbors(v: int):
        """ return (i-j) for (i, j) where i+j = v """
        assert v not in init_a
        for i in range(max(0, v-y+1), min(x, v+1)):
            b = 2*i - v  # i-j = i-(v-i) = 2i-v
            if b not in init_b:
                yield b

    matches = bipartite_match(set(range(0, x + y - 1)) - init_a, neighbors)

    for a, b in matches.items():
        i = (a + b) // 2
        j = (a - b) // 2
        board[i, j] |= PLUS


def eval_score(board):
    score = 0
    for model in np.nditer(board):
        if model & CROSS != 0:
            score += 1
        if model & PLUS != 0:
            score += 1
    return score


def augment_fashion_show(n, models):
    shape = (n, n)
    board = np.zeros(shape, dtype=int)
    for symbol, x, y in models:
        board[x-1, y-1] = parse_symbol(symbol)

    original = np.copy(board)
    place_cross(board)
    place_plus(board)

    printer = []
    for i in range(0, n):
        for j in range(0, n):
            if board[i, j] != original[i, j]:
                printer.append('{symbol} {x} {y}'.format(
                    symbol=encode_model(board[i, j]),
                    x=i+1, y=j+1))

    return '{score} {num_lines}\n{models}'.format(
        score=eval_score(board),
        num_lines=len(printer),
        models='\n'.join(printer)).rstrip()


def parser(reader):
    n, num_models = map(int, reader.readline().split())
    models = []
    for _ in range(num_models):
        symbol, x, y = reader.readline().split()
        models.append((symbol, int(x), int(y)))

    return augment_fashion_show(n, models)

if __name__ == '__main__':
    codejam.run(parser, open('fashion-show-large.in', 'r'), open('fashion-show-large.out', 'w'))
