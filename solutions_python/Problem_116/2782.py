# -*- coding: utf-8 -*-
from operator import add


with open('A-small-attempt0.in', 'r') as input:
    with open('A-small-attempt0.out', 'w') as output:
        T = int(input.readline())

        directions = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [0, 5, 10, 15], [3, 6, 9, 12]]

        for index in range(1, T + 1):

            board = reduce(add, [input.readline().strip() for i in range(4)])
            input.readline()

            empty = False
            win = None

            for line in directions:
                turn = None
                count = 0
                for i in line:
                    if board[i] == '.':
                        empty = True
                    elif board[i] == 'T':
                        count += 1
                    elif turn is None:
                        turn = board[i]
                        # print 'turn = ',board[i], i
                        count = 1
                        # if index == 6: print 'xd'
                    elif board[i] == turn:
                        count += 1
                    # else:
                        # if index == 6: print turn
                # if index == 6: print count
                if count == 4:
                    win = turn
                    break

            if win:
                output.write('Case #%i: %s won\n' % (index, turn))
            elif empty:
                output.write('Case #%i: Game has not completed\n' % index)
            else:
                output.write('Case #%i: Draw\n' % index)
