# coding: UTF-8
 
import sys, copy

class Case:
    def __init__(self, num, naomi, ken):
        self.num = num
        self.naomi = naomi
        self.ken = ken

def readFile():     
    argvs = sys.argv 
    argc = len(argvs)
    if argc is not 2:
        quit()
    f = open(argvs[1])
    num_test = int(f.readline().strip())
    cases = []
    for i in range(num_test):
        blocks = int(f.readline().strip())
        naomi = [float(x) for x in f.readline().split(' ')] 
        ken = [float(x) for x in f.readline().split(' ')] 
        cases.append(Case(blocks, naomi, ken))
    if num_test is not len(cases):
        raise 0
    return num_test, cases

def solveNormal(case):
    point = 0
    naomi = copy.deepcopy(case.naomi)
    naomi.sort()
    ken = copy.deepcopy(case.ken)
    ken.sort()
    for n in naomi:
        tmp = [x for x in ken if n < x ]
        if not tmp:
            ken = ken[1:]
            point += 1
        else:
            tmp.sort()
            ken.remove(tmp[0])
    return point

def solveDeceitful(case):
    point = 0
    naomi = copy.deepcopy(case.naomi)
    naomi.sort()
    ken = copy.deepcopy(case.ken)
    ken.sort()
    for n in naomi:
        larger = [x for x in ken if n > x]
        if not larger:
            ken = ken[:-1]
        else:
            larger.sort()
            larger.reverse()
            ken.remove(larger[0])
            point += 1
    return point

def solveSub(case):
    return solveDeceitful(case), solveNormal(case)

def solve(num_test, cases):
    for i in range(num_test):
        deceitful, normal = solveSub(cases[i])
        print "Case #"+str(i+1)+": " + str(deceitful)+" "+str(normal)

def main():
    num_test, cases = readFile()
    solve(num_test, cases)

main()
