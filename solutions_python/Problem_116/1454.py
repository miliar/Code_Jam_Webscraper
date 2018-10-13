import sys

def check_line(line):
    counts = {'.': 0, 'X':0, 'O':0, 'T':0 }
    for c in line:
        counts[c] = counts[c] + 1
    if counts['T'] == 1:
        to_win = 3
    else:
        to_win = 4
    if counts['X'] == to_win:
        return 'X'
    elif counts['O'] == to_win:
        return 'O'
    elif counts['.'] == 0:
        return "full"
    else:
        return None

def check_results(table):
    # check lines
    game_over = True
    for line in table:
        res = check_line(line)
        if res == 'X' or res == 'O':
            return res + " won"
        if res == None:
            game_over = False
    # check columns
    for i in xrange(4):
        line = [l[i] for l in table]
        res = check_line(line)
        if res == 'X' or res == 'O':
            return res + " won"
    # check diagonals
    diags = []
    diags.append([table[i][i] for i in xrange(4)])
    diags.append([table[i][3 - i] for i in xrange(4)])
    for d in diags:
        res = check_line(d)
        if res == 'X' or res == 'O':
            return res + " won"
    if game_over:
        return "Draw"
    else:
        return "Game has not completed"
        

# read cases from stdin
if __name__ == "__main__":
    f = sys.stdin
    T = int(f.readline())
    for case in xrange(1, T + 1):
        table = []
        for line in f:
            line = line.strip()
            if len(line) == 0:
                break
            table.append(line)
        print "Case #%s: %s" % (case, check_results(table))
