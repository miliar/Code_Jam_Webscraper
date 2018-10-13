import os
import itertools
patterns = itertools.chain(["".join(a) for a in itertools.permutations('XXXT', 4)],
                           ["".join(a) for a in itertools.permutations('OOOT', 4)],
                           ['XXXX', 'OOOO'])
patterns = set(patterns)

count = 1
def _info(s):
    global count
    print "Case #%d: %s" % (count, s)
    count += 1

def win(line):
    if line in patterns:
        if "XX" in line:
            _info("X won")
        else:
            _info("O won")
        return True
    return False

def docal(box):
    if not box:
        return
    notc = False
    for line in box:
        notc = notc or '.' in line
        if win(line):
            return
    for i in range(4):
        line = "".join([a[i] for a in box])
        if win(line):
            return
    line = "".join([box[i][i] for i in range(4)])
    if win(line):
        return
    line = "".join([box[3 - i][i] for i in range(4)])
    if win(line):
        return
    if notc:
        _info("Game has not completed")
    else:
        _info("Draw")


with open("A-large.in") as f:
    lines = f.read().split("\n")[1:]

box = []
for line in lines:
    if line:
        box.append(line)
    else:
        docal(box)
        box = []
if box:
    docal(box)
