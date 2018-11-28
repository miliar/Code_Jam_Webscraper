import sys

inp = sys.stdin.read().splitlines()[1:]

def check(s):
    if s in ['XXXX', 'XXXT', 'XXTX', 'XTXX', 'TXXX']:
        return 'X'
    elif s in ['OOOO', 'OOOT', 'OOTO', 'OTOO', 'TOOO']:
        return 'O'
    else:
        return None

for T in xrange(0, len(inp), 5):
    cur = inp[T:T+4]
    winner = None
    for i in range(4):
        winner = winner or check(cur[i][0] + cur[i][1] + cur[i][2] + cur[i][3])
        winner = winner or check(cur[0][i] + cur[1][i] + cur[2][i] + cur[3][i])
    winner = winner or check(cur[0][0] + cur[1][1] + cur[2][2] + cur[3][3])
    winner = winner or check(cur[0][3] + cur[1][2] + cur[2][1] + cur[3][0])
    if winner:
        outcome = winner + ' won'
    elif '.' in ''.join(cur):
        outcome = 'Game has not completed'
    else:
        outcome = 'Draw'
    print 'Case #%d: %s' % (T/5 + 1, outcome)
