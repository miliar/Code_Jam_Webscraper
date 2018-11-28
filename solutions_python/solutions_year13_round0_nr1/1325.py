import sys
import re

fin = sys.stdin
fout = sys.stdout

def char_to_int(char):
    if (char == 'X'):
        return 13
    elif (char == 'O'):
        return 17
    elif (char == 'T'):
        return 10
    elif (char == '.'):
        return 0
    else:
        return -1

def X_win(num):
    return (num == 52 or num == 49)

def O_win(num):
    return (num == 68 or num == 61)

def dotestcase(ii):
    rows = []

    for jj in range (0, 4, 1):
        rows.append(fin.readline())
        pass
    fin.readline()

    for row in rows:
        num = (char_to_int(row[0]) + char_to_int(row[1]) +
               char_to_int(row[2]) + char_to_int(row[3]))
        if (X_win(num)):
            fout.write("Case #" + str(ii + 1) + ": X won\n")
            return
        elif (O_win(num)):
            fout.write("Case #" + str(ii + 1) + ": O won\n")
            return

    for jj in range (0, 4, 1):
        num = (char_to_int(rows[0][jj]) + char_to_int(rows[1][jj]) +
               char_to_int(rows[2][jj]) + char_to_int(rows[3][jj]))
        if (X_win(num)):
            fout.write("Case #" + str(ii + 1) + ": X won\n")
            return
        elif (O_win(num)):
            fout.write("Case #" + str(ii + 1) + ": O won\n")
            return

    num = (char_to_int(rows[0][0]) + char_to_int(rows[1][1]) +
           char_to_int(rows[2][2]) + char_to_int(rows[3][3]))
    if (X_win(num)):
        fout.write("Case #" + str(ii + 1) + ": X won\n")
        return
    elif (O_win(num)):
        fout.write("Case #" + str(ii + 1) + ": O won\n")
        return

    num = (char_to_int(rows[0][3]) + char_to_int(rows[1][2]) +
           char_to_int(rows[2][1]) + char_to_int(rows[3][0]))
    if (X_win(num)):
        fout.write("Case #" + str(ii + 1) + ": X won\n")
        return
    elif (O_win(num)):
        fout.write("Case #" + str(ii + 1) + ": O won\n")
        return

    for row in rows:
        num = (char_to_int(row[0]) + char_to_int(row[1]) +
               char_to_int(row[2]) + char_to_int(row[3]))
        if (num < 49):
            fout.write("Case #" + str(ii + 1) + ": Game has not"
                       + " completed\n")
            return

    for jj in range (0, 4, 1):
        num = (char_to_int(rows[0][jj]) + char_to_int(rows[1][jj]) +
               char_to_int(rows[2][jj]) + char_to_int(rows[3][jj]))
        if (num < 49):
            fout.write("Case #" + str(ii + 1) + ": Game has not"
                       + " completed\n")
            return

    num = (char_to_int(rows[0][0]) + char_to_int(rows[1][1]) +
           char_to_int(rows[2][2]) + char_to_int(rows[3][3]))
    if (num < 49):
        fout.write("Case #" + str(ii + 1) + ": Game has not"
                   + " completed\n")
        return

    num = (char_to_int(rows[0][3]) + char_to_int(rows[1][2]) +
           char_to_int(rows[2][1]) + char_to_int(rows[3][0]))
    if (num < 49):
        fout.write("Case #" + str(ii + 1) + ": Game has not"
                   + " completed\n")
        return

    fout.write("Case #" + str(ii + 1) + ": Draw\n")
    
T = int(fin.readline())
for ii in range (0, T, 1):
    dotestcase(ii)
