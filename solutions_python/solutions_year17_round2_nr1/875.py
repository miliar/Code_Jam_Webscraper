from decimal import *
import sys
from math import sqrt
from collections import deque
#my_dict.pop('key', None)
sys.setrecursionlimit(1500)
in_file = open('A-large.in', 'r')
out_file = open('A-large-answer.in', 'w')

def solve(destiny, others):
    for i in range(len(destiny)):
        destiny[i] = int(destiny[i])
    for i in range(len(others)):
        for j in range(len(others[i])):
            others[i][j] = int(others[i][j])
    holsetime = []
    for i in range(len(others)):
        time = Decimal((destiny[0] - others[i][0]) / others[i][1])
        holsetime.append(time)
    answer = []
    for i in range(len(holsetime)):
        answer.append(Decimal(destiny[0] / holsetime[i]))
    return min(answer)


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
    twolinelist = []
    for new in range(int(onelinelist[1])):
        q += 1
        temp = p[q].strip().split()
        twolinelist.append(temp)
    answer = solve(onelinelist, twolinelist)
    print("Case #%d: " % (i) + str(answer))
    out_file.write("Case #%d: " % (i) + str(answer) + '\n')
    i += 1
    q += 1