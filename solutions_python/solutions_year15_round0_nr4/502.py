import sys
import numpy as np
from pprint import pprint

numTests = int(sys.stdin.readline().rstrip("\n"))

class Point:
    def _init_(self,x,y):
        self.x = x
        self.y = y

def gen(points,p,X):
    if( X == 0):
        return [points]

    output = []
    perms = [(0,1),(1,0),(0,-1),(-1,0)]

    for nxt in perms:
        cand = (p[0] + nxt[0],p[1] + nxt[1])

        if cand in points:
            continue

        new_points = points[:]
        new_points.append(cand)
        rs = gen(new_points,cand,X-1)
        output.extend(rs)

    return output

class Domino:
    def __init__(self,piece):
        self.points = piece[:]

def can_solve(piece,R,C):
    grid = np.zeros((R,C))

# sorry for the hacks, but the input size is just sooo small and I'm so tired..
full_table = dict()
full_table[1] = [
    [True,True,True,True],
    [True,True,True,True],
    [True,True,True,True],
    [True,True,True,True],
]

full_table[2] = [
    [False,True,False,True],
    [True,True,True,True],
    [False,True,False,True],
    [True,True,True,True],
]

full_table[3] = [
    [False,False,False,False],
    [False,False,True,False],
    [False,True,True,True],
    [False,False,True,False],
]

full_table[4] = [
    [False,False,False,False],
    [False,False,False,False],
    [False,False,False,True],
    [False,False,True,True],
]

for i in xrange(numTests):
    X,R,C = sys.stdin.readline().rstrip("\n").split(" ")
    X = int(X)
    R = int(R)
    C = int(C)

    if( full_table[X][R-1][C-1]):
        print("Case #"+ str(i + 1) + ": GABRIEL")
    else:
        print("Case #"+ str(i + 1) + ": RICHARD")

    # perms = gen([(0,0)],(0,0),X-1)
    # for piece in d.perms:
    #     d = Domino(piece)
    #     can_solve(d,R,C)
    # print("Case #"+ str(i + 1) + ": NO")