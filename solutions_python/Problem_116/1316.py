import sys, pprint

lines = open(sys.argv[1],'rb').readlines()
T = int(lines[0])

X_MATCHES = set(['XXXX', 'XXXT','XXTX','XTXX','TXXX'])
Y_MATCHES = set(['OOOO', 'OOOT','OOTO','OTOO','TOOO'])
_FOUR = range(4)

def get_game_status(state):
    state.extend([
        ''.join([state[i][i] for i in _FOUR]),
        ''.join([state[i][3-i] for i in _FOUR])
    ])
    for j in _FOUR:
        state.append(''.join([state[i][j] for i in _FOUR]))
    empty_slot = False
    for s in state:
        #print '--%s--' % s
        if s in X_MATCHES:
            return 'X won'
        elif s in Y_MATCHES:
            return 'O won'
        empty_slot = empty_slot or '.' in s
    return 'Game has not completed' if empty_slot else 'Draw'

lines = lines[1:]
lines = [l.strip() for l in lines]
for i in range(T):
    print 'Case #%d: %s' % (i+1, get_game_status(lines[i*5:4+i*5]))
