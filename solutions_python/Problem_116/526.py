import sys

WAIT_TOTAL = 0
WAIT_LINE = 1

DRAW = 'Draw'
PLAYING = 'Game has not completed'
WON = 'won'

def process_input():

    cases_count = 0
    lines = []
    lines_count = 0

    state = WAIT_TOTAL
    for line in sys.stdin.readlines():
        line = line.strip()
        if line != '':

            if state == WAIT_TOTAL:
                c = int(line)
                state = WAIT_LINE
            elif state == WAIT_LINE:
                lines.append(list(line))
                lines_count += 1
                if lines_count == 4:
                    cases_count += 1
                    assert cases_count <= c
                    ret = process_case(lines)
                    sys.stdout.write('Case #' + str(cases_count) + ': ')
                    print ret
                    lines_count = 0
                    lines = []
            else:
                assert False

def process_case(table):
    win = map(lambda x: winning(x), table)
    win = filter(lambda x: x != None, win)
    if win != []:
        return ' '.join([win[0], WON])

    diag = diagonal(table)
    if diag != None:
        return ' '.join([diag, WON])

    table = transpose(table)

    win = map(lambda x: winning(x), table)
    win = filter(lambda x: x != None, win)
    if win != []:
        return ' '.join([win[0], WON])

    diag = diagonal(table)
    if diag != None:
        return ' '.join([diag, WON])

    draw = map(lambda x: not full(x), table)
    draw = filter(lambda x: x != True, draw)
    if len(draw) == 0:
        return DRAW

    return PLAYING

def diagonal(table):
    first = table[0][0] if table[0][0] != 'T' else table[1][1]
    diag = True
    for i in range(1,4):
        if table[i][i] != first and table[i][i] != 'T':
            diag = False

    if not diag or first == '.':
        first = table[0][3] if table[0][3] != 'T' else table[1][2]
        if first == '.':
            return None
        diag = True
        for i in range(1,4):
            if table[i][3-i] != first and table[i][3-i] != 'T':
                diag = False

    return first if diag else None

def transpose(table):
    return zip(*table)

def winning(row):
    first = row[0] if row[0] != 'T' else row[1]
    if first == '.':
        return None
    ret = filter(lambda x: x != first and x != 'T', row)
    return first if len(ret) == 0 else None

def full(row):
    return len(filter(lambda x: x != 'T' \
            and x != 'O' \
            and x != 'X', row)) != 0




process_input()

