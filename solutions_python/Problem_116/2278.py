#!/usr/bin/python
#encoding: utf-8

import re
#Tic-Tac-Toe-Tomek

x_winner = re.compile('[XT]{4}', re.I)
o_winner = re.compile('[OT]{4}', re.I)

def check_winner(board, winner = ''):
    new_winner = winner
    for line in board:
        is_x_winner = x_winner.match(line)
        is_o_winner = o_winner.match(line)
        if is_x_winner != None and is_x_winner.span() == (0, 4):
            new_winner += 'X'
        if is_o_winner != None and is_o_winner.span() == (0, 4):
            new_winner += 'O'
    return new_winner


def cols_to_rows(board):
    inverted_board = ['','','','']
    for i in range(0, 4):
        inverted_board[i] = board[0][i] + board[1][i] + board[2][i] + board[3][i]
    return inverted_board

def get_diagonals(board):
    diagonal_1 = board[0][0] + board[1][1] + board[2][2] + board[3][3]
    diagonal_2 = board[3][0] + board[2][1] + board[1][2] + board[0][3]
    return (diagonal_1, diagonal_2)

def full_board(board):
    for i in range(0, 4):
        if board[i].find('.') >= 0:
            return False
    return True

input_file = open('A-large.in', 'rU')

boards = [l.rstrip() for l in input_file.readlines()]

input_file.close()

boards =[line for line in boards if line]
number_of_cases = int(boards.pop(0))
boards = [boards[i:i+4] for i in range(0, len(boards), 4)]
inverted_boards = map(cols_to_rows, boards)
diagonals = map(get_diagonals, boards)

results = []

for i in range(0, number_of_cases):
    is_board_full = full_board(boards[i])
    winner = check_winner(boards[i])
    if(winner == ''):
        winner = check_winner(inverted_boards[i], winner)
    if(winner == ''):
        winner = check_winner(diagonals[i], winner)
    results.append((is_board_full, winner))

output = open('A-large-output.out', 'w')
output_string = "Case #%d: %s\n"

for i in range(0, number_of_cases):
    if results[i][0] == True:
        if results[i][1] == '':
            output.write(output_string % (i + 1, 'Draw'))
        elif results[i][1] == 'X':
            output.write(output_string % (i + 1, 'X won'))
        elif results[i][1] == 'O':
            output.write(output_string % (i + 1, 'O won'))
        elif len(results[i][1]) > 1:
            print results[i]
    else:
        if results[i][1] == '':
            output.write(output_string % (i + 1, 'Game has not completed'))
        elif results[i][1] == 'X':
            output.write(output_string % (i + 1, 'X won'))
        elif results[i][1] == 'O':
            output.write(output_string % (i + 1, 'O won'))
        elif len(results[i][1]) > 1:
            print results[i]
output.close()



