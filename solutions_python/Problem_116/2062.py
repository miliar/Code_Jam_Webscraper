#!/usr/bin/env python
import sys
from pprint import pprint
from multiprocessing import Pool

ELEM_MAP = {'.': 0, 'O': 1, 'X': 2, 'T': 3}
RESULTS = {0: 'Game has not completed', 1: 'O won', 2: 'X won', 3: 'Draw'}
def main(filename):
    boards = []
    with open(filename, "r") as f:
        no_of_elements = int(f.readline().strip())
        for __ in range(no_of_elements):
            board = []
            for __ in range(4):
                line = f.readline().strip()
                elements = [ELEM_MAP[c] for c in line]
                board.append(elements)
            boards.append(board)
            if f.readline().strip():
                raise Exception("Unexpected non-empty line")

    winners = []
    with Pool(processes=8) as pool:
        for case, board in enumerate(boards, 1):
            winner = pool.apply_async(check_winner, [board])
            winners.append((case, winner.get()))
    sorted(winners, key=lambda t: t[0])
    with open("{0}_out".format(filename), "w") as f:
        lines = []
        for case, winner in winners:
            lines.append("Case #{0}: {1}".format(case, RESULTS[winner]))
        f.write("\n".join(lines))


def check_winner(board):
    done = True
    for row in board:
        if 0 in row:
            done = False
            continue
        player = get_player(row)
        if player == 0:
            continue
        return player

    for i in range(4):
        col = [row[i] for row in board]
        if 0 in col:
            done = False
            continue
        player = get_player(col)
        if player == 0:
            continue
        return player

    diag1 = [board[i][i] for i in range(4)]
    player = get_player(diag1)
    if player != 0:
        return player
    diag2 = [board[3 - i][i] for i in range(4)]
    player = get_player(diag2)
    if player != 0:
        return player
    return 3 if done else 0

def get_player(dataset):
    if 0 in dataset:
        return 0
    dataset_sum = sum(dataset)
    if dataset_sum == 4 or dataset_sum == 6:
        if 2 not in dataset:
            return 1
    elif dataset_sum == 8 or dataset_sum == 9:
        if 1 not in dataset:
            return 2
    return 0
            



if __name__ == '__main__':
    main(sys.argv[1])
