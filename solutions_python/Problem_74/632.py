#!/usr/bin/env python
import sys

###
O = "O"
B = "B"

class Robot(object):
    def __init__(self, color):
        self.color = color
        self.cur = 1
        self.target = []

    def move(self, turn):
        pushed = False
        if len(self.target) == 0:
            move = "stay at %d"
        else:
            if self.cur == self.target[0]:
                # already reached there
                if turn == self.color:
                    move = "push %d"
                    pushed = True
                    self.target = self.target[1:]
                else:
                    move = "stay at %d"
            else:
                if self.cur > self.target[0]:
                    self.cur -= 1
                else:
                    self.cur += 1
                move = "move to %d"

        return (pushed, move % self.cur)

def solve(case):
    robot = { O:Robot(O), B:Robot(B) }
    target = makedic(case)
    robot[O].target = target[O]
    robot[B].target = target[B]

    tic = 0
    moves = {}
    for i in range(1, len(case), 2):
        turn = case[i]
        reached = False
        while not reached:
            for color in (O, B):
                (result, move) = robot[color].move(turn)
                reached = reached or result 
                moves[color] = move
            print("%4d | %s | %s" % (tic, moves[O], moves[B]))
            tic += 1
    
    return tic


def makedic(case):
    N = int(case[0])
    move = { "B":[], "O":[] }
    for i in range(1, N * 2, 2):
        move[case[i]].append(int(case[i + 1]))
    return move

###    
def readinput(file):
    print("reading %s ..." % file)

    f = open(file, "r")
    N = int(f.readline())
    cases = []
    for line in f:
        cases.append(line.split())
    f.close()

    print("%d records read." % len(cases))
    if len(cases) != N:
        print("Warning: number of cases mismatch")
    return cases

#
# main
#
if len(sys.argv) < 2:
    print("Usage: %s filename" % sys.argv[0])
#    sys.exit(1)
#file = sys.argv[1]
file = "A-small-attempt0.in.in.in"
cases = readinput(file)

out = open(file + ".output", "w")
n = 1
for case in cases:
    msg = "Case #%d: %d" % (n, solve(case)) 
    print(msg)
    out.write(msg + "\n")
    n += 1
