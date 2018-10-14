# encoding: UTF-8
#Google Code Jam 2017 Round1C
#Problem B

import collections
import itertools
import sys

class gcj:
    identity = lambda x: x

    @classmethod
    def _read_line_raw(cls):
        line = in_file.readline()
        if not line:
            raise EOFError()
        return line.rstrip('\r\n')

    @classmethod
    # read single character
    def token(cls, conv=identity):
        line = cls._read_line_raw()
        return conv(line)

    @classmethod
    # read multiple single characters splitted by sep
    def tokens(cls, conv=identity, sep = ' '):
        line = cls._read_line_raw()
        return [conv(i) for i in line.split(sep)]

    current_case = 0

    @classmethod
    def case(cls):
        cls.current_case += 1
        return('Case #{}: '.format(cls.current_case))

def solve():
    AC, AJ = gcj.tokens(int)
    N = AC + AJ
    Clist = []
    Jlist = []
    worklist = []
    for _ in range(AC):
        s,e = gcj.tokens(int)
        worklist.append([s,e,0])
    for _ in range(AJ):
        s,e = gcj.tokens(int)
        worklist.append([s,e,1])
    worklist.sort(key=lambda x: x[0])
    blank = []
    moreblank = []
    lessblank = []
    change = 0
    time1 = 0
    timemax = 1440
    st = worklist[0][0]
    worklist = [[x[0]-st,x[1]-st,x[2]] for x in worklist]
    worklist.append([timemax,timemax,worklist[0][2]])

    present = worklist[0][2]
    for i,x in enumerate(worklist):
        if x[2] != present:
            change += 1
            present = x[2]
            if present == 0:
                time1 += x[1]-x[0]
                blank.append(x[0]-worklist[i-1][1])
            else:
                blank.append(x[0]-worklist[i-1][1])
        elif i>0:
            if present == 0:
                time1 += x[1]-worklist[i-1][1]
                lessblank.append(x[0]-worklist[i-1][1])
            else:
                moreblank.append(x[0]-worklist[i-1][1])
        else:
            if present == 0:
                time1 += x[1]-x[0]
    lessblank.sort(reverse=True)
    moreblank.sort(reverse=True)
    diff = time1 - timemax//2
    if diff < 0:
        diff += sum(blank)
        if diff >= 0:
            return(str(change))
        else:
            i = 0
            while diff < 0:
                diff += moreblank[i]
                change += 2
                i += 1
            return(str(change))
    else:
        diff -= sum(blank)
        if diff <= 0:
            return(str(change))
        else:
            i = 0
            while diff > 0:
                diff -= lessblank[i]
                change += 2
                i += 1
            return(str(change))


def main():
    sys.setrecursionlimit(9999)
    t = gcj.token(int)
    # t = 1
    for _ in range(t):
        case = gcj.case()
        solution = solve()
        out_file.write(case+solution+"\n")
        print(case+solution)
        sys.stdout.flush()

# problem_name = 'B-small'
problem_name = 'B-small-attempt0'
in_file = open(problem_name+'.in',"r")
out_file = open(problem_name+'.out', "w")
main()
in_file.close()
out_file.close()