# encoding: UTF-8
#Google Code Jam 2017 Round1C
#Problem A

import collections
import itertools
import sys
import operator
import math

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
    pi = math.pi
    N, K = gcj.tokens(int)
    p = []
    for _ in range(N):
        r,h = gcj.tokens(int)
        p.append([r**2, 2*r*h])
    p.sort(key=lambda x: tuple([x[0],x[1]]),reverse=True)
    maxS = 0
    # print(p)
    for i in range(N-K+1):
        Surface = 0
        Surface += p[i][0] + p[i][1]
        pconc = [x[1] for x in p[i+1:N]]
        pconc.sort(reverse=True)
        Surface += sum(pconc[0:K-1])
        maxS = max(maxS,Surface)
    maxS *= pi

    return('{:.8f}'.format(maxS))
    


def main():
    sys.setrecursionlimit(9999)
    t = gcj.token(int)
    # t = 5
    for _ in range(t):
        case = gcj.case()
        solution = solve()
        out_file.write(case+solution+"\n")
        print(case+solution)
        sys.stdout.flush()

problem_name = 'A-large'
in_file = open(problem_name+'.in',"r")
out_file = open(problem_name+'.out', "w")
main()
in_file.close()
out_file.close()