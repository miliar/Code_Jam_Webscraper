# encoding: UTF-8
#Google Code Jam 2017 Round1B
#Problem A

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
    D,N = gcj.tokens(int)
    data = []
    for _ in range(N):
        data.append(gcj.tokens(int))
    maxarrival = 0
    for i,val in enumerate(data):
        maxarrival = max(maxarrival, (D-val[0])/val[1])
    maxvel = D/maxarrival
    return(str(maxvel))



def main():
    sys.setrecursionlimit(9999)
    t = gcj.token(int)
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