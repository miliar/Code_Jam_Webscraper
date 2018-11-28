#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Régis Décamps"

import sys

def read_input(file):
    matrix = []
    for i in range(4):
        line = file.readline()
        # remove leading \n
        matrix.append(line.strip())
    return matrix


def has_won(player, matrix):
    return has_won_h(player, matrix) or has_won_v(player, matrix) or has_won_d(player, matrix)


def has_won_h(player, matrix):
    for i in range(4):
        placed = sum((1 if (matrix[i][j]==player or matrix[i][j]=='T') else 0 for j in range(4)))
        if placed==4:
            return True
    return False


def has_won_v(player, matrix):
    for j in range(4):
        placed = sum((1 if (matrix[i][j]==player or matrix[i][j]=='T') else 0 for i in range(4)))
        if placed==4:
            return True
    return False


def has_won_d(player, matrix):
    return has_won_d1(player, matrix) or has_won_d2(player, matrix)


def has_won_d1(player, matrix):
    for i in range(4):
        if matrix[i][i] != player and matrix[i][i] != 'T':
            return False
    return True


def has_won_d2(player, matrix):
    for i in range(4):
        j = 3 - i
        if matrix[i][j] != player and matrix[i][j] != 'T':
            return False
    return True


def game_not_completed(matrix):
    for line in matrix:
        if '.' in line:
            return True
    return False


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        nb_games = int(f.readline()) + 1
        for i in range(1, nb_games):
            matrix = read_input(f)

            if has_won('O', matrix):
                print("Case #{i}: O won".format(i=i))
            elif has_won('X', matrix):
                print("Case #{i}: X won".format(i=i))
            elif game_not_completed(matrix):
                print("Case #{i}: Game has not completed".format(i=i))
            else:
                print("Case #{i}: Draw".format(i=i))
                #empty line
            if i < nb_games:
                f.readline()