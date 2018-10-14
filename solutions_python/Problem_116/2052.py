import sys

def result(board):
    WILD = 'T'
    EMPTY = '.'
    unfinished = False

    for i in range(4):
        board.append([board[j][i] for j in range(4)])
    board.append([board[i][i] for i in range(4)])
    board.append([board[i][3-i] for i in range(4)])

    for line in board:
        line_set = set(line)
        if EMPTY in line_set:
            unfinished = True 
            continue;
        if WILD in line_set:
            line_set.discard(WILD)
        if len(line_set) == 1:
            return "{} won".format(next(iter(line_set)))
    
    if (unfinished):
        return 'Game has not completed' 
    else:
        return 'Draw'

def main(argv):
    if len(argv) != 2:
        sys.exit('Usage: python filename.py <input_file> <output_file>')
    with open(argv[0], 'r') as data, open(argv[1], 'w+') as output:
        lines = map(lambda s: s.strip(), data.readlines())
        step = 5
        case = 1
        for i in range(1, len(lines), step):
            board = [list(b) for b in lines[i:i+step-1]]
            solution = result(board)
            output.write("Case #{}: {}\n".format(case, solution))
            case += 1
    data.close()
    output.close()


if __name__ == '__main__':
    main(sys.argv[1:])
