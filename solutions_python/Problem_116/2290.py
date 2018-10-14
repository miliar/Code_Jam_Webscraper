import re
import sys

lines = [
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11],
    [12,13,14,15]
]

columns = [
    [0,4,8,12],
    [1,5,9,13],
    [2,6,10,14],
    [3,7,11,15]
]

diagonal = [
    [0,5,10,15],
    [3,6,9,12]
]

def score(table):
    winner = winner_is(table)
    if winner:
        return winner
    if has_moves(table):
        return 'Game has not completed'
    else:
        return 'Draw'

def get_moves(table):
    player_x = []
    player_o = []

    line = re.sub(r"\s", "", table)
    assert len(line) == 16
    for i,l in enumerate(line):
        if l == 'T':
            player_x.append(i)
            player_o.append(i)
        if l == 'X':
            player_x.append(i)
        elif l == 'O':
            player_o.append(i)
    return (player_x, player_o)

def winner_is(table):
    px, po = get_moves(table)
    win_moves = lines + columns + diagonal
    for w in win_moves:
        if set(w) <= set(px):
            return 'X won'
        elif set(w) <= set(po):
            return 'O won'
    return False

def has_moves(table):
    return '.' in table

def report(case):
    m = re.match(r'^(\d+)\n', case)
    n = int(m.group(0))
    case = re.sub(r'^(\d+)\n', '', case)
    data = case.strip().split('\n\n')
    assert n == len(data), 'Error %d != %d' % (n, len(data))
    output = []
    for i,c in enumerate(data):
        output.append('Case #%d: %s' % (i+1, score(c)))
    return '\n'.join(output)

def main(args, dry = False):
    if len(args) > 1:
        f = open(args[1])
        data = f.read()
        f.close()
        output = report(data)
        if dry:
            return output
        f = open(args[1] + '.output','w')
        f.write(output)
        f.close()

if __name__ == '__main__':
    main(sys.argv)