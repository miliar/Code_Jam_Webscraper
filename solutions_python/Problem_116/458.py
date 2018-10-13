import sys

args = sys.argv

if len(args) < 2:
    print 'small or large?'
    exit()

inp = args[1]

out = open(inp + '_OUT', 'w')

# No change before this

def check_win(s, player):
    if s.count(player) == 4:
        return True
    if s.count(player) == 3 and s.find('T') >= 0:
        return True
    return False

def solve():
    rows = []
    cols = ['']*4
    ds = ['']*2
    finished = True
    for i in xrange(4):
        row = raw_input()
        if row.find('.') >= 0:
            finished = False
        rows.append(row)
        for j in xrange(4):
            if i == j:
                ds[0] += row[j]
            if i + j == 3:
                ds[1] += row[j]
            cols[j] += row[j]
    empty_line = raw_input()
    data = rows + cols + ds

    for d in data:
        if check_win(d, 'X'):
            return 'X won'
        if check_win(d, 'O'):
            return 'O won'
    if finished:
        return 'Draw'
    return 'Game has not completed'

T = input()
for i in xrange(1, T+1):
    ans = 'Case #' + str(i) + ': ' + solve()
    print ans
    out.write(ans + '\n')
# No change after this

out.close()
