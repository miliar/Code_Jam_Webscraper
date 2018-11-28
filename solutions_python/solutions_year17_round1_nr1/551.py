#!/usr/bin/env python

import sys

M = []
R = -1
C = -1

def getFirstNotEmpty(row):
    if row > 0:
        return row - 1
    
    for row in range(row+1,R) :
        if all(value != '?' for value in M[row]) :
            return row

def addFirstValueNotEmpty(rowA, colA):
    value = None
    for row in range(rowA-1, -1, -1) :
        if M[row][colA] != '?' :
            value = M[row][colA]
    
    if value is not None:
        M[rowA][colA] = value

    if existsConflict():
        for row in range(rowA+1, R) :
            if M[row][colA] != '?' :
                return M[row][colA]

        if value is not None:
            M[rowA][colA] = value

def existsConflict():
    for row in range(R) :
        for col in range(C) :
            if M[row][col] != '?':
                found_r = -1
                found_c = -1
                for row2 in range(row,R) :
                    for col2 in range(col,C) :
                        if M[row][col] == M[row2][col2]:
                            if row2 > found_r:
                                found_r = row2
                            if col2 > found_c:
                                found_c = col2
                # print(row, col, found_r, found_c, file=sys.stderr)

                for row2 in range(row,found_r+1) :
                    for col2 in range(col,found_c+1) :
                        if M[row][col] != M[row2][col2]:
                            return True
                            # print("ERROR", row, col, row2, col2, file=sys.stderr)

    return False


def solve():
    global M

    for row in range(R) :
        char = '?'
        for col in range(C) :
            if M[row][col] != '?':
                char = M[row][col]
            elif char != '?':
                M[row][col] = char
                if existsConflict():
                    addFirstValueNotEmpty(row, col)


    for row in range(R) :
        char = '?'
        for col in range(C-1,-1,-1) :
            if M[row][col] != '?':
                char = M[row][col]
            elif char != '?':
                M[row][col] = char
                if existsConflict():
                    addFirstValueNotEmpty(row, col)

    for row in range(R) :
        if all(value == '?' for value in M[row]) :
            new_row = getFirstNotEmpty(row)
            for col in range(C) :
                M[row][col] = M[new_row][col]


def main():
    global M
    global R
    global C
    case_counter = 1

    T = int(input())  # read a line with a single integer

    for i in range(1, T + 1):
        
        # INPUT
        R, C = [int(s) for s in input().split(" ")]
        # print("N: ", N)
        # print("K: ", K)
        M = []
        [M.append(list(input())) for x in range(R)]
        # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in M]))
        # print(M)

        # SOLVE
        solve()

        # OUTPUT
        print("Case #{}:".format(case_counter))
        # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in M]))
        print('\n'.join([''.join(['{}'.format(item) for item in row]) for row in M]))
        case_counter += 1


if  __name__ =='__main__':
    main()
