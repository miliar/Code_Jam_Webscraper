# coding: UTF-8
 
import sys

class Case:
    def __init__(self, c, f, x):
        self.c = c
        self.f = f
        self.x = x

def readFile():     
    argvs = sys.argv 
    argc = len(argvs)
    if argc is not 2:
        quit()
    f = open(argvs[1])
    num_test = int(f.readline().strip())
    cases = []
    for i in range(num_test):
        line = [float(x) for x in f.readline().split(' ')]
        if len(line) != 3:
            print line
            raise 0
        cases.append(Case(line[0], line[1], line[2]))
    if num_test is not len(cases):
        raise 0
    return num_test, cases
"""
def solveSubSub(case, f_time):
    time = 0.0
    f = 2.0
    cookie = 0.0
    clock = 0.0001
    while(True):
        time += 
        if case.x <= cookie:
            return time
        if case.c <= cookie:
            cookie -= case.c
            f += case.f
        cookie += f * clock
        time += clock
"""

def solveSubSub(case, f_times):
    time = 0.0
    f = 2.0
    for i in range(f_times):
        time += case.c / f
        f += case.f
    time += case.x / f
    return time

def solveSub(case):
    minTime = 2000.0
    for i in range(0, 2001):
        time = solveSubSub(case, i)
        if time < minTime:
            minTime = time
    return minTime
    #return min(solveSubSub(case, 500))

def solve(num_test, cases):
    for i in range(num_test):
        t = solveSub(cases[i])
        formatted = '%.7f' % (t)
        print "Case #"+str(i+1)+": "+formatted

def main():
    num_test, cases = readFile()
    solve(num_test, cases)

main()
