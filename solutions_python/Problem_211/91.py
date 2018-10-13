# encoding: UTF-8
#Google Code Jam 2017 Round1C
#Problem C

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
    N,K = gcj.tokens(int)
    U = gcj.token(float)
    P = gcj.tokens(float)
    avg = (sum(P)+U)/N
    under = [i for i in P if i<avg]
    over = [i for i in P if i>=avg]
    if len(under)>0:
        newavg = (sum(under)+U)/len(under)
    prob = 1
    for i in under:
        prob *= newavg
    for j in over:
        prob *= j
    return('{:.8f}'.format(prob))


def main():
    sys.setrecursionlimit(9999)
    t = gcj.token(int)
    # t = 2
    for _ in range(t):
        case = gcj.case()
        solution = solve()
        out_file.write(case+solution+"\n")
        print(case+solution)
        sys.stdout.flush()

problem_name = 'C-small-1-attempt0'
in_file = open(problem_name+'.in',"r")
out_file = open(problem_name+'.out', "w")
main()
in_file.close()
out_file.close()