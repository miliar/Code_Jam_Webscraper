#! /usr/bin/env python

def main():
    boards = []
    numboards = int(raw_input())
    for i in xrange(numboards):
        boards.append(readboard())
        if i != numboards - 1:
            raw_input()
    i = 0
    for board in boards:
        i += 1
        print "Case #" + str(i) + ": " + gamestatus(board)

def gamestatus(board):
    if gamewon("X",board):
        return "X won"
    elif gamewon("O",board):
        return "O won"
    elif spaceAvailable(board):
        return "Game has not completed"
    else:
        return "Draw"

def gamewon(player, board):
    for i in xrange(4):
        # horizontal search
        if linewon(player, board[i]):
            return True
        # vertical search
        if linewon(player, [line[i] for line in board]):
            return True
    # diagonals
    if linewon(player,[board[i][i] for i in xrange(4)]) or linewon(player, [board[i][3-i] for i in xrange(4)]):
        return True
    return False


def linewon(player, line):
    for char in line:
        if char != player and char != "T":
            return False
    return True

def spaceAvailable(board):
    for line in board:
        if "." in line:
            return True
    return False


def readboard():
    board = []
    for i in xrange(4):
        board.append(list(raw_input()))
    return board


if __name__=='__main__':
    main()