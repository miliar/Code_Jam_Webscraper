#!/usr/bin/env python
# -*- coding: utf-8 -*-


def readData():
    emptyLine = 0
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        for i in xrange(n):
            for rowIndex, line in enumerate(f):
                if line == '\n':
                    emptyLine += 1
                yield (rowIndex - emptyLine) % 4, line

def writeData(data):
    with open('output.txt', 'w') as fout:
        fout.write('\n'.join(data))


def solution():
    answer = []

    x_array = [[{'row': 0, 'column': 0, 'diag': 0, 'adiag': 0} for i in xrange(6)] for j in xrange(6)]
    o_array = [[{'row': 0, 'column': 0, 'diag': 0, 'adiag': 0} for i in xrange(6)] for j in xrange(6)]
    emptyField = False
    case = 0

    for rowIndex, line in readData():
        if line == '\n':
            case += 1
            winner = ''

            for i in xrange(1, 5):
                for j in xrange(1, 5):
                    if x_array[i][j]['row'] == 4 or x_array[i][j]['column'] == 4 or \
                        x_array[i][j]['diag'] == 4 or x_array[i][j]['adiag'] == 4:
                        winner = 'X'
                        break
            
            for i in xrange(1, 5):
                for j in xrange(1, 5):
                    if o_array[i][j]['row'] == 4 or o_array[i][j]['column'] == 4 or \
                        o_array[i][j]['diag'] == 4 or o_array[i][j]['adiag'] == 4:
                        winner = 'O'
                        break
    
            if winner != '':
                answer.append('Case #{0}: {1} won'.format(case, winner))
            else:
                if emptyField:
                    answer.append('Case #{0}: Game has not completed'.format(case))
                else:
                    answer.append('Case #{0}: Draw'.format(case))

            x_array = [[{'row': 0, 'column': 0, 'diag': 0, 'adiag': 0} for i in xrange(6)] for j in xrange(6)]
            o_array = [[{'row': 0, 'column': 0, 'diag': 0, 'adiag': 0} for i in xrange(6)] for j in xrange(6)]
            emptyField = False 

        else:
            for columnIndex, field in enumerate(line):
                if field == 'X' or field == 'T':
                    x_array[rowIndex + 1][columnIndex + 1]['row'] = x_array[rowIndex + 1][columnIndex]['row'] + 1
                    x_array[rowIndex + 1][columnIndex + 1]['column'] = x_array[rowIndex][columnIndex + 1]['column'] + 1
                    x_array[rowIndex + 1][columnIndex + 1]['diag'] = x_array[rowIndex][columnIndex]['diag'] + 1
                    x_array[rowIndex + 1][columnIndex + 1]['adiag'] = x_array[rowIndex][columnIndex + 2]['adiag'] + 1

                if field == 'O' or field == 'T':
                    o_array[rowIndex + 1][columnIndex + 1]['row'] = o_array[rowIndex + 1][columnIndex]['row'] + 1
                    o_array[rowIndex + 1][columnIndex + 1]['column'] = o_array[rowIndex][columnIndex + 1]['column'] + 1
                    o_array[rowIndex + 1][columnIndex + 1]['diag'] = o_array[rowIndex][columnIndex]['diag'] + 1
                    o_array[rowIndex + 1][columnIndex + 1]['adiag'] = o_array[rowIndex][columnIndex + 2]['adiag'] + 1

                if field == '.':
                    emptyField = True
    
    writeData(answer)


if __name__ == "__main__":
    solution()
