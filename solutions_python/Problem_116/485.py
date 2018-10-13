X_WINS = 0
O_WINS = 1
TIE = 2
INCOMPLETE = 3


def solve(config):
    # check rows
    for row in range(4):
        x = 0
        o = 0
        for col in range(4):
            if config[row][col] == 'X':
                x += 1
            elif config[row][col] == 'O':
                o += 1
            elif config[row][col] == 'T':
                x += 1
                o += 1
            else:
                break

        if x == 4:
            return X_WINS
        elif o == 4:
            return O_WINS

    # check cols
    for col in range(4):
        x = 0
        o = 0
        for row in range(4):
            if config[row][col] == 'X':
                x += 1
            elif config[row][col] == 'O':
                o += 1
            elif config[row][col] == 'T':
                x += 1
                o += 1
            else:
                break

        if x == 4:
            return X_WINS
        elif o == 4:
            return O_WINS

    # check diagonals
    # topleft to bottom right
    col = 0
    x = 0
    o = 0
    for row in range(4):
        if config[row][col] == 'X':
            x += 1
        elif config[row][col] == 'O':
            o += 1
        elif config[row][col] == 'T':
            x += 1
            o += 1
        else:
            break
        col += 1

    if x == 4:
        return X_WINS
    elif o == 4:
        return O_WINS

    # topright to bottomleft
    col = 3
    x = 0
    o = 0
    for row in range(4):
        if config[row][col] == 'X':
            x += 1
        elif config[row][col] == 'O':
            o += 1
        elif config[row][col] == 'T':
            x += 1
            o += 1
        else:
            break
        col -= 1

    if x == 4:
        return X_WINS
    elif o == 4:
        return O_WINS

    # check if full or incomplete
    for row in range(4):
        for col in range(4):
            if config[row][col] == '.':
                return INCOMPLETE
    return TIE


def main():
    f = open("in.txt")
    lines = f.readlines()

    num_tests = int(lines[0].strip())

    configs = []

    line_no = 1

    for i in range(num_tests):
        configs.append([])
        for j in range(4):
            configs[i].append([letter for letter in lines[line_no].strip()])
            #configs[i].append(lines[line_no].strip())
            line_no += 1
        line_no += 1

    case_num = 1
    for config in configs:
        ret = solve(config)
        if ret == X_WINS:
            print "Case #" + str(case_num) + ": X won"
        elif ret == O_WINS:
            print "Case #" + str(case_num) + ": O won"
        elif ret == TIE:
            print "Case #" + str(case_num) + ": Draw"
        elif ret == INCOMPLETE:
            print "Case #" + str(case_num) + ": Game has not completed"
        case_num += 1


if __name__ == '__main__':
    main()
