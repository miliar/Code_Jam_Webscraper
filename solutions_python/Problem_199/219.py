from decimal import *
from math import log10
from collections import deque
in_file = open('A-large.in', 'r')
out_file = open('finish.in', 'w')
temp = {}
getcontext().prec = 20
##k = Decimal(allsuc * (left + back + 1) + (1 - allsuc) * ((left + back + 1) + arr1[1] + 1))

def solve(flip, c):
    k = []
    count = 0
    for i in flip:
        k.append(i)
    for i in range(len(k)):
        try:
            if k[i] == '-':
                count += 1
                for j in range(c):
                    if k[i + j] == '-':
                        k[i + j] = '+'
                    else:
                        k[i + j] = '-'

        except:
            return 'IMPOSSIBLE'
    return count

p = []
for line in in_file:
    p.append(line)
n = p[0]
q = 1
i = 1
answer = None
ques = []
getcontext().prec = 20
while q < len(p):
    m = p[q].strip().split()
    answer = solve(m[0], int(m[1]))
    print("Case #%d: " % (i) + str(answer))
    i += 1
    q += 1