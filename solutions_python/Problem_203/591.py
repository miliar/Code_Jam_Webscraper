from decimal import *
from math import log10
from collections import deque
from math import gcd

#in_file = open('A-large.in', 'r')
in_file = open('A-large.in', 'r')
out_file = open('A-large-answer.in', 'w')
getcontext().prec = 100

def solve(childlist):
    diction = dict()
    for i in range(len(childlist)):
        for j in range(len(childlist[i])):
            if childlist[i][j] != '?':
                if childlist[i][j] in diction:
                    continue
                else:
                    diction[childlist[i][j]] = 1
                a = helper(childlist, i + 1, j, childlist[i][j], 1)
                b = helper(childlist, i - 1, j, childlist[i][j], 1)
    answer = '\n'
    dict2 = dict()
    for i in range(len(childlist)):
        for j in range(len(childlist[i])):
            if childlist[i][j] != '?':
                helper2(childlist, i, j + 1, childlist[i][j], 1)
                helper2(childlist, i, j - 1, childlist[i][j], 1)
    for i in range(len(childlist)):
        for j in range(len(childlist[i])):
            answer += childlist[i][j]
        answer += '\n'
    answer = answer[:-1]
    return answer

def helper(childlist, i, j, ori, count):
    if i < 0 or j < 0 or i == len(childlist) or j == len(childlist[i]) or childlist[i][j] != '?':
        return count
    else:
        childlist[i][j] = ori
        a = helper(childlist, i + 1, j, ori, count + 1)
        b = helper(childlist, i - 1, j, ori, count + 1)
    return max(a, b)

def helper2(childlist, i, j, ori, count):
    if i < 0 or j < 0 or i == len(childlist) or j == len(childlist[i]) or childlist[i][j] != '?':
        return count
    else:
        childlist[i][j] = ori
        a = helper2(childlist, i, j + 1, ori, count + 1)
        b = helper2(childlist, i, j - 1, ori, count + 1)
    return max(a, b)

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
    onelinelist = p[q].strip().split()
    secondmatrix = []
    for one in range(int(onelinelist[0])):
        q += 1
        newmatrix = p[q].strip().split()
        simple = []
        for letter in newmatrix:
            for alpha in letter:
                simple.append(alpha)
        secondmatrix.append(simple)
    answer = solve(secondmatrix)
    print("Case #%d: " % (i) + str(answer))
    out_file.write("Case #%d: " % (i) + str(answer) + '\n')
    i += 1
    q += 1