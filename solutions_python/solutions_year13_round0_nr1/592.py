#!/usr/bin/env python
import sys
from collections import defaultdict

def classify(line):
    who_won = None
    has_empty = False
    counts = defaultdict(int)
    board_size = len(line)
    for c in line:
        counts[c] += 1
    if counts['O'] + counts['T'] == board_size:
        who_won = 'O'
    elif counts['X'] + counts['T'] == board_size:
        who_won = 'X'
    elif counts['.']:
        has_empty = True
    return who_won, has_empty

def main():
    num_tests = int(sys.stdin.readline())
    board_size = 4
    for test_id in range(1, num_tests + 1):
        if test_id > 1:
            sys.stdin.readline()
        board = []
        for _ in range(board_size):
            board.append(sys.stdin.readline().strip())
            assert(len(board[-1]) == board_size)
        who_won = None
        has_empty = False
        for line in board:
            if who_won is not None:
                break
            w, h = classify(line)
            if w is not None:
                who_won = w
            has_empty |= h
        for col in range(board_size):
            if who_won is not None:
                break
            line = "".join([board[row][col] for row in range(board_size)])
            w, h = classify(line)
            if w is not None:
                who_won = w
            has_empty |= h

        w, h = classify("".join([board[i][i] for i in range(board_size)]))
        if w is not None:
            who_won = w
        has_empty |= h

        w, h = classify("".join(
                [board[i][board_size - i - 1] for i in range(board_size)]))
        if w is not None:
            who_won = w
        has_empty |= h
        if who_won is None:
            if has_empty:
                message = "Game has not completed"
            else:
                message = "Draw"
        else:
            message = "%s won" % who_won

        print "Case #%d: %s" % (test_id, message)



if __name__ == "__main__":
    main()
