from decimal import *
import sys
from math import sqrt
from collections import deque
#my_dict.pop('key', None)
sys.setrecursionlimit(1500)
in_file = open('C-small-1-attempt0.in', 'r')
out_file = open('C-small-answer.in', 'w')

def solve(kind, bonus, core):
    getcontext().prec = 17
    minimum = int(kind[1])
    bonus = Decimal(bonus[0])
    for i in range(len(core)):
        core[i] = Decimal(core[i])
    core.sort()
    maxnumber = Decimal(0)
    for i in range(len(core)):
        maxnumber += core[i]
    maxnumber = maxnumber / len(core)
    while bonus > 0:
        n = 1
        i = 0
        target = 0
        while True:
            if i == len(core) - 1:
                n = len(core)
                target = 1
                break
            elif core[i] < core[i + 1]:
                target = core[i + 1]
                break
            else:
                i += 1
                n += 1
        want = Decimal((target - core[0]) * n)
        if bonus >= want:
            bonus -= want
            give = Decimal(want / n)
            for i in range(n):
                core[i] += Decimal(give)
        else:
            give = bonus / n
            bonus = 0
            for i in range(n):
                core[i] += Decimal(give)
        if core[0] == 1:
            break
    answer = 1
    for i in range(len(core)):
        answer *= core[i]
    return answer

p = []
for line in in_file:
    p.append(line)
n = p[0]
q = 1
i = 1
answer = None
ques = []
getcontext().prec = 30
while q < len(p):
    onelinelist = p[q].strip().split()
    q += 1
    two = p[q].strip().split()
    q += 1
    three = p[q].strip().split()
    answer = solve(onelinelist, two, three)
    print("Case #%d: " % (i) + str(answer))
    out_file.write("Case #%d: " % (i) + str(answer) + '\n')
    i += 1
    q += 1