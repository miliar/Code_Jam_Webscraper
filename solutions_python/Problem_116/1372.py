
import sys
from collections import *
sn = sys.stdin

class xy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return xy(self.x + other.x,
                  self.y + other.y)

T = int(sn.readline())
for it in range(T):
    board = [sn.readline() for i in range(4)]
    sn.readline()

    starts = [xy(x, 0) for x in range(4)] \
           + [xy(0, y) for y in range(4)] \
           + [xy(0, 0), xy(3, 0)]
    dirs = [xy(0, 1)] * 4 \
         + [xy(1, 0)] * 4 \
         + [xy(1, 1), xy(-1, 1)]
    traces = []
    for i in range(len(starts)):
        tr = [starts[i]]
        for k in range(3):
            tr.append(tr[-1] + dirs[i])
        traces.append(tr)

    has_dots = False
    state = None
    for tr in traces:
        here = []
        for coord in tr:
            here.append(board[coord.y][coord.x])
        c = Counter(here)
        nx = c['X']
        no = c['O']
        nt = c['T']
        ndot = c['.']
        if ndot >= 1:
            has_dots = True
        if 4 == nx + nt:
            state = "X won"
        elif 4 == no + nt:
            state = "O won"
        
    if None == state:
        state = "Draw" if False == has_dots else "Game has not completed"

    print "Case #%d:" % (it+1), state


