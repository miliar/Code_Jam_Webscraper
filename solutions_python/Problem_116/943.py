__author__ = 'israel.roth@gmail.com'

import datetime


def check_sequence_for_winner(l):
    nT = l.count('T')
    nX = l.count('X') + nT
    if nX == 4:
        return True, "X won", 0
    nO = l.count('O') + nT
    if nO == 4:
        return True, "O won", 0
        return
    nEmpty = l.count('.')
    return False, "", nEmpty


def game_result(l1, l2, l3, l4):
    rows = [list(l1), list(l2), list(l3), list(l4)]
    cols = [
            [rows[0][0], rows[1][0], rows[2][0], rows[3][0]],
            [rows[0][1], rows[1][1], rows[2][1], rows[3][1]],
            [rows[0][2], rows[1][2], rows[2][2], rows[3][2]],
            [rows[0][3], rows[1][3], rows[2][3], rows[3][3]]
            ]

    totEmpty = 0
    # check if there is a winner in rows
    for row in rows:
        found_winner, str, nEmpty = check_sequence_for_winner(row)
        if found_winner:
            return str
        totEmpty += nEmpty
    # check if there is a winner in columns
    for col in cols:
        found_winner, str, nEmpty = check_sequence_for_winner(col)
        if found_winner:
            return str
    # check for winner in diagonals
    found_winner, str, nEmpty = check_sequence_for_winner([rows[0][0], rows[1][1], rows[2][2], rows[3][3]])
    if found_winner:
        return str
    found_winner, str, nEmpty = check_sequence_for_winner([rows[0][3], rows[1][2], rows[2][1], rows[3][0]])
    if found_winner:
        return str

    if totEmpty > 0:
        return "Game has not completed"
    else:
        return "Draw"

# ok, get test cases...

testfile = open ('TicTacToeTomek.in')
line = testfile.readline()
ntests = int(line)

outfile = open('TicTacToeTomek.out', 'w')

print datetime.datetime.now()

for testnum in range(0,ntests):
    l1 = testfile.readline()
    l2 = testfile.readline()
    l3 = testfile.readline()
    l4 = testfile.readline()
    lskip = testfile.readline()

    result = game_result(l1,l2,l3,l4)

    # sys.stdout.write(".")
    outfile.write ("Case #"+str(testnum+1)+": " + result + "\n")
    print ("Case #"+str(testnum+1)+": " + result)


print datetime.datetime.now()
