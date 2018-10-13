# coding: UTF-8
 
import sys

class Arrange:
    def __init__(self, row, arrange):
        self.row = row
        self.arrange = arrange

class Case:
    def __init__(self, first_row, first_arrange,\
                     second_row, second_arrange):
        self.first = Arrange(first_row, first_arrange)
        self.second = Arrange(second_row, second_arrange)
        
def readFile():     
    argvs = sys.argv 
    argc = len(argvs)
    if argc is not 2:
        quit()
    f = open(argvs[1])
    num_test = int(f.readline().strip())
    cases = []
    for i in range(num_test):
        first_row = int(f.readline().strip())
        first_arrange = []
        for j in range(4):
            first_arrange.append( \
                f.readline().strip().split(' '))
        second_row = int(f.readline().strip())
        second_arrange = []
        for j in range(4):
            second_arrange.append( \
                f.readline().strip().split(' '))
        cases.append(Case(first_row, first_arrange, \
                           second_row, second_arrange))
    if num_test is not len(cases):
        raise 0
    return num_test, cases

def solveSub(first, second):
    return [x for x in first if x in second]

def solve(num_test, cases):
    for i in range(num_test):
        first_contain = cases[i].first.arrange[ \
            cases[i].first.row - 1]
        second_contain = cases[i].second.arrange[ \
            cases[i].second.row - 1]
        same_num = solveSub(first_contain, second_contain)
        if len(same_num) == 1:
            print "Case #"+str(i+1)+": "+str(same_num[0])
        elif 1 < len(same_num):
            print "Case #"+str(i+1)+": Bad magician!"
        else:
            print "Case #"+str(i+1)+": Volunteer cheated!"

def main():
    num_test, cases = readFile()
    solve(num_test, cases)

main()
