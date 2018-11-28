#program to determine the state of play of a board of tic-tac-toe-tomek, google code jam 2013 qualification round q. A. (https://code.google.com/codejam/contest/2270488/dashboard)

import sys

ARGS = sys.argv
#input file
FIN = open(ARGS[1], 'r')

#Number of test cases
T = int(FIN.readline()[:-1])
print "T, T+1", T, T+1

#List of test cases. Each test case is a list of four strings, representing the rows of the board.
TESTCASES = []
for i in range(T):
    #list to accumulate the four strings
    x = []
    for j in range(4):
        x.append(FIN.readline()[:-1])
    FIN.readline()
    TESTCASES.append(x)
print "TESTCASES:", TESTCASES

#function to decide if X has won or not
def xwon(testcase):
    x_replaced_testcase = ['', '', '', '']
    for i in range(4):
        x_replaced_testcase[i] = replacechar(testcase[i], 'T', 'X')
    if charwon(x_replaced_testcase, 'X'):
        return 1
    else:
        return 0
#function to decide if O has won or not
def owon(testcase):
    o_replaced_testcase = ['', '', '', '']
    for i in range(4):
        o_replaced_testcase[i] = replacechar(testcase[i], 'T', 'O')
    if charwon(o_replaced_testcase, 'O'):
        return 1
    else:
        return 0

#function to decide if a certain character has won:
def charwon(testcase, char):
    if rowwon(testcase, char) or columnwon(testcase, char) or diagwon(testcase, char):
        return 1
    else:
        return 0

#function to replace a character
def replacechar(string, to_replace, replace_with):
    #replacement string
    result = ''
    for i in range(len(string)):
        if string[i] == to_replace:
            result += replace_with
        else:
            result += string[i]
    return result

#function to decide if a character has won in a string
def stringwon(string, winchar):
    result = 1
    for char in string:
        if char == winchar:
            result *= 1
        else:
            result *=0
    return result
#functions to decide if a character has won by row, column, or diagonal
def rowwon(testcase, winchar):
    result = 0
    for string in testcase:
        result += stringwon(string, winchar)
    return result
#function to transpose columns into rows
def transpose(testcase):
    result = ['','','','']
    for i in range(4):
        result[i] = testcase[0][i] + testcase[1][i] + testcase[2][i] + testcase[3][i]
    return result
def columnwon(testcase, winchar):
    result = 0
    for string in transpose(testcase):
        result += stringwon(string, winchar)
    return result

#function to transpose diagonals into rows
def transpose_d(testcase):
    result = ['', '']
    result[0] = testcase[0][0] + testcase[1][1] + testcase[2][2] + testcase[3][3]
    result[1] = testcase[0][3] + testcase[1][2] + testcase[2][1] + testcase[3][0]
    return result
def diagwon(testcase, winchar):
    result = 0
    for string in transpose_d(testcase):
        result += stringwon(string, winchar)
    return result

#function decides if there are any spaces (represented by '.') left in the board
def spaceleft(testcase):
    result = 0
    for string in testcase:
        for char in string:
            if char == '.':
                result += 1
            else:
                pass
    return result

print 'testing spaceleft', spaceleft(['XXXT', '....', 'OO..', '....']), spaceleft(['XXXX', 'OOOO', 'XOXO', 'XXXO'])

#main function to decide what state the board is in
def main(testcase):
    if xwon(testcase):
        return "X won"
    elif owon(testcase):
        return "O won"
    elif spaceleft(testcase):
        return "Game has not completed"
    else:
        return "Draw"

print 'testing owon:', owon(['XXXO', '..O.', '.O..', 'T...'])

for i in range(T):
    print "Case #%i:" %(i+1), main(TESTCASES[i])
