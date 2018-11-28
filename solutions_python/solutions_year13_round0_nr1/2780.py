fileout = 'output.txt'
filename = 'A-small-attempt0.in'

responses = {1: 'X won', 2: 'O won', 3: 'Draw', 4: 'Game has not completed'}


def load_file(filename):
    lines = [line.strip() for line in open(filename)]
    cases = int(lines[0])
    mat = []
    for i in range(1, cases + 1):
        start_line = (i - 1) * 5 + 1
        block = []
        for j in range(start_line, start_line + 4):
            line = lines[j]
            row = [line[k] for k in range(len(line))]
            block.append(row)
        mat.append(block)
    return mat


def extendCol(block, j):
    char = block[j][0]
    if char == 'O' or char == 'X' or char == 'T':
        for k in range(1, 4):
            spot = block[j][k]
            if (not spot == char) and (not spot == 'T') and (char == 'T'):
                char = spot
            elif (not spot == char) and (not spot == 'T'):
                return False, 0
        return True, char
    return False, 0


def extendRow(block, k):
    char = block[0][k]
    if char == 'O' or char == 'X' or char == 'T':
        for j in range(1, 4):
            spot = block[j][k]
            if char == 'O' or char == 'X' or char == 'T':
                if (not spot == char) and (not spot == 'T') and (char == 'T'):
                    char = spot
                elif (not spot == char) and (not spot == 'T'):
                    return False, 0
            else:
                return False, 0
        return True, char
    return False, 0


def extend_dia_left(block):
    char = block[0][0]
    if char == 'O' or char == 'X' or char == 'T':
        for i in range(1, 4):
            spot = block[i][i]
            if char == 'O' or char == 'X' or char == 'T':
                if (not spot == char) and (not spot == 'T') and (char == 'T'):
                    char = spot
                elif (not spot == char) and (not spot == 'T'):
                    return False, 0
            else:
                return False, 0
        return True, char
    return False, 0


def extend_dia_right(block):
    char = block[0][3]
    if char == 'O' or char == 'X' or char == 'T':
        for i in range(1, 4):
            spot = block[i][3 - i]
            if char == 'O' or char == 'X' or char == 'T':
                if (not spot == char) and (not spot == 'T') and (char == 'T'):
                    char = spot
                elif (not spot == char) and (not spot == 'T'):
                    return False, 0
            else:
                return False, 0
        return True, char
    return False, 0


def isWin(block):
    finished = True
    for i in range(0, 4):
        if block[i][i] == '.':
            finished = False
        result_row = extendRow(block, i)
        if result_row[0]:
            char = result_row[1]
            if char == 'X':
                return 1
            if char == 'O':
                return 2

        result_col = extendCol(block, i)
        if result_col[0]:
            char = result_col[1]
            if char == 'X':
                return 1
            if char == 'O':
                return 2

        result_dia_left = extend_dia_left(block)
        if result_dia_left[0]:
            char = result_dia_left[1]
            if char == 'X':
                return 1
            if char == 'O':
                return 2

        result_dia_right = extend_dia_right(block)
        if result_dia_right[0]:
            char = result_dia_right[1]
            if char == 'X':
                return 1
            if char == 'O':
                return 2

    if not finished:
        return 4
    elif finished:
        return 3


if __name__ == '__main__':
    mat = load_file(filename)
    f = open(fileout, 'w')
    for i in range(len(mat)):
        res = isWin(mat[i])
        case = str(i + 1)
        print "Case #" + case + ": " + responses.get(res)
        f.writelines("Case #" + case + ": " + responses.get(res) + "\n")
    f.close()
