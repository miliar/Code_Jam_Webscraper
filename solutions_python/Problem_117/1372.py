#!/usr/bin/python

f = open("B-large.in", 'r')
out = open("B-large.out", 'w')
T = int(f.readline())

outs = ["NO", "YES"]

def search(board, i, j):
    # first test row
    for jind in range(len(board[i])):
        if board[i][jind] > board[i][j]:
            break
    else:
        return True

    # now check col
    for iind in range(len(board)):
        if board[iind][j] > board[i][j]:
            break
    else:
        return True

    return False


for n in range(T):
    N, M = (int(x) for x in f.readline().split())

    board = []
    for j in range(N):
        board.append([int(x) for x in f.readline().split()])

    output = "Case #%d: %s\n"
    done = False
    good = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not search(board, i, j):
                good = False
                done = True
                break

        if done:
            break

    out.write(output % (n+1, outs[good]))


out.close()
f.close()
