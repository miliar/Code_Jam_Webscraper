#!/usr/bin/python


def check(l1):
    RESULT = ''
    for i in l1:
        if '.' in i:
            RESULT = 'Game has not completed'
            break

    if RESULT == '':
        RESULT = 'Draw'

    #check for diagnal winner
    d1 = [l1[0][0], l1[1][1], l1[2][2], l1[3][3]]
    T = d1.count('T')
    X = d1.count('X') + T
    if X == 4:
        return 'X won'

    O = d1.count('O') + T
    if O == 4:
        return 'O won'

    d1 = [l1[3][0], l1[2][1], l1[1][2], l1[0][3]]
    T = d1.count('T')
    X = d1.count('X') + T
    if X == 4:
        return 'X won'

    O = d1.count('O') + T
    if O == 4:
        return 'O won'

    #Check row winner
    for i in range(0, 4):
        T = l1[i].count('T')
        X = l1[i].count('X') + T
        if X == 4:
            return 'X won'

        O = l1[i].count('O') + T
        if O == 4:
            return 'O won'

    #check column winner
    for i in range(0, 4):
        abc = {'X': 0, 'O': 0, 'T': 0, '.': 0}
        for j in range(0, 4):
            stri = l1[j][i]
            abc[stri] += 1
        if abc['X'] + abc['T'] == 4:
            return 'X won'
        if abc['O'] + abc['T'] == 4:
            return 'O won'
    return RESULT

lines = {}
counter = -1
linesnr = 0
for line in open('inp', 'r'):
    line = line.strip()
    if counter == -1:
        linesnr = int(line)
        counter += 1
        continue
    if line == '':
        counter += 1
    else:
        try:
            lines[counter].append(line)
        except:
            lines[counter] = [line]

counter = 0
result = []
while counter < linesnr:
    result.append(check(lines[counter]))
    counter += 1


counter = 0
file = open('output', 'w')
while counter < linesnr:
    file.write('Case #' + str(counter+1) + ': ' + result[counter] + '\n')
    counter += 1
