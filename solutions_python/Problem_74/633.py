#!/usr/bin/python

#input = [(0, 2), (1, 1), (1, 2), (0, 4)]
#input = [(0, 5), (0, 8), (1, 100)]
#input = [(1, 2), (1, 1)]


def other(b): return 0 if b == 1 else 1
def b2s(b): return "Orange" if b == 1 else "Blue"

def solve(input):
    total = [0,0]
    pos = [1,1]
    lastb = -1

    for b, s in input:
        time = abs(pos[b]-s)

        if b == lastb:
            total[b] += time + 1
        elif total[other(b)] > total[b] + time:
            total[b] = total[other(b)] + 1
        else:
            total[b] += time + 1
        pos[b] = s
        lastb = b



    #print("Input: %s" % input)
    #print(b2s(b))
    #print("Time: %d" % time)
    #print("Total: %d" % total[b])
    #print("Pos: %d" % pos[b])
    #print("-----")

    return max(total)

import fileinput
import re
f = fileinput.input()
numLines = int(f.next())

case = 1
for line in f:
    m = re.match(r"(\d+) (.*)", line)
    cc = int(m.group(1))
    commands = zip(*[iter(m.group(2).split())]*2)
    commands = map(lambda x: (0 if x[0] == 'O' else 1, int(x[1])), commands)
    print("Case #%d: %d" % (case, solve(commands)))
    case += 1


