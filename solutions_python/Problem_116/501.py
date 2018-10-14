#!/usr/bin/env python3

PROBLEM_LETTER = 'A'
DIFFICULTY = 'large'
INPUT_FILE = '{0}-{1}.in'.format(PROBLEM_LETTER, DIFFICULTY)
OUTPUT_FILE = '{0}-{1}.out'.format(PROBLEM_LETTER, DIFFICULTY)

def won(field, player):
    def goodSet(row):
        return row.count(player) == 4 or (row.count(player) == 3 and row.count('T') == 1)

    for row in field:
        if goodSet(row): return True
    transposed = zip(*field)
    for col in transposed:
        if goodSet(col): return True
    if goodSet([field[0][0], field[1][1], field[2][2], field[3][3]]): return True
    if goodSet([field[0][3], field[1][2], field[2][1], field[3][0]]): return True
    return False

if __name__ == "__main__":
    fin = open(INPUT_FILE, 'r')
    fout = open(OUTPUT_FILE, 'w')

    testCount = int(fin.readline())
    for i in range(testCount):
        field = list(range(4))
        for j in range(4):
            field[j] = fin.readline()
        fin.readline()
        if won(field, 'X'): fout.write('Case #{0}: X won\n'.format(i + 1))
        elif won(field, 'O'): fout.write('Case #{0}: O won\n'.format(i + 1))
        elif any('.' in r for r in field): fout.write('Case #{0}: Game has not completed\n'.format(i + 1))
        else: fout.write('Case #{0}: Draw\n'.format(i + 1))

    fin.close()
    fout.close()