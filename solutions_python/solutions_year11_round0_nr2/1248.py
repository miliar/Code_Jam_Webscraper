#!/usr/bin/env python2
import sys

def solve(case, combs, opps):
    answer = list()
    for c in case:
        i = len(answer)
        answer.append(c)
        if i > 0 and c in combs and combs[c][0] in answer[i-1]:
            del answer[i-1:i]
            answer[i-1] = combs[c][1]
        elif c in opps and opps[c] in answer:
            answer = []
    if answer == case:
        return answer
    return solve(answer, combs, opps)
            

def printcase(number, case):
    sys.stdout.write('Case #' + str(number+1) + ': [')
    for c in case[:-1]:
        sys.stdout.write(c + ', ')
    if case == []:
        sys.stdout.write(']\n')
    else:
        sys.stdout.write(case[-1] + ']\n')

lines = [ line.split() for line in sys.stdin.readlines()[1:] ]
cases = list()
combinations = list()
opposed = list()

for i,l in enumerate(lines):
    combs = int(l[0])
    combinations.insert(i,dict())
    for j in xrange(1, combs + 1):
        combinations[i][l[j][0]] = l[j][1:]
        combinations[i][l[j][1]] = l[j][0] + l[j][2]

    opps = int(l[combs + 1])
    opposed.insert(i, dict())
    for j in xrange(combs + 2, combs + 2 + opps):
        opposed[i][l[j][0]] = l[j][1]
        opposed[i][l[j][1]] = l[j][0]

    cases.insert(i, list())
    for c in l[-1]:
        cases[i].append(c)

for i, case in enumerate(cases):
    printcase(i, solve(case, combinations[i], opposed[i]))


