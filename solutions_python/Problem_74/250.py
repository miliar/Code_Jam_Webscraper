import sys
from collections import defaultdict

class Robot:
    def __init__(self, buttons):
        self.moves = buttons
        self.pos = 1

    def move(self, canPush):
        if self.moves:
            if self.pos < self.moves[0]:
                self.pos += 1
            elif self.pos > self.moves[0]:
                self.pos -= 1
            elif canPush:
                self.moves = self.moves[1:]
                return True
            else:
                return False
        else:
            return True

n = int(input())
for case in range(1, n+1):
    mlist = input().split()
    mlist = mlist[1:]

    Omoves = []
    Mmoves = []
    for i in range(0, len(mlist), 2):
        if mlist[i] == "O":
            Omoves.append(int(mlist[i+1]))
        elif mlist[i] == "B":
            Mmoves.append(int(mlist[i+1]))
        else:
            print("WTFMOVE", mlist[i], i)

    M = Robot(Mmoves)
    O = Robot(Omoves)

    count = 0
    while mlist:
        count += 1
        active = mlist[0]
        if active == "B":
            if M.move(True):
                mlist = mlist[2:]
            O.move(False)
        elif active == "O":
            if O.move(True):
                mlist = mlist[2:]
            M.move(False)
        else:
            print("WTFACTIVE", mlist[i], i)
    print("Case #" + str(case) + ":", count)
