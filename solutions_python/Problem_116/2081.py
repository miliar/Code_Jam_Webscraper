import sys
from pprint import pprint

X_WON = "X won"
O_WON = "O won"
DRAW = "Draw"
NOT_DONE = "Game has not completed"

# [[(0, 0), (0, 1), (0, 2), (0, 3)],
#  [(1, 0), (1, 1), (1, 2), (1, 3)],
#  [(2, 0), (2, 1), (2, 2), (2, 3)],
#  [(3, 0), (3, 1), (3, 2), (3, 3)],
#  [(0, 0), (1, 0), (2, 0), (3, 0)],
#  [(0, 1), (1, 1), (2, 1), (3, 1)],
#  [(0, 2), (1, 2), (2, 2), (3, 2)],
#  [(0, 3), (1, 3), (2, 3), (3, 3)],
#  [(0, 3), (1, 2), (2, 1), (3, 0)]]
POSSIBLE_SET = [[ (j, i) for i in range(4)] for j in range(4)] + \
               [[ (i, j) for i in range(4)] for j in range(4)] + \
               [[ (i, i) for i in range(4)]] + \
               [[ (i, 3-i) for i in range(4)]]

def CheckWin(state, team):
    result = [ map(lambda pos: state[pos[0]][pos[1]] == team or state[pos[0]][pos[1]] == 'T', case)
            for case in POSSIBLE_SET ]
    return any(map(lambda case_solution: all(case_solution), result))



def CheckStatus(state):
    if CheckWin(state, 'O'):
        return O_WON
    if CheckWin(state, 'X'):
        return X_WON
    if any([any(map(lambda x:x=='.', row)) for row in state]):
        return NOT_DONE
    return DRAW

def ReadData():
    rl = sys.stdin.readline
    n = int(rl())
    for i in range(n):
        state = [
        rl().strip(),
        rl().strip(),
        rl().strip(),
        rl().strip(),
        ]
        rl()
        print("Case #%d: %s"%(i+1, CheckStatus(state)))

ReadData()

