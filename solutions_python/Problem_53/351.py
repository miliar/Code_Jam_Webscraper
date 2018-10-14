import sys
from itertools import *

def solve(input_line, case_no):
    N, K = map(lambda x: int(x.strip()), input_line.split(' '))
    print "Solving: #%s N=%s, K=%s" % (case_no, N, K)
    space = pow(2,N)
    on = bool(space - 1 == (K % space))
    return "ON" if on else "OFF"

fn = sys.argv[1]
input = iter(open(fn, 'r'))
output = open(fn.replace('.in', '.out'), 'w')

T = int(input.next().strip())

for case_no in range(T):
    solution = solve(input.next().strip(), case_no)
    print >>output, "Case #%d: %s"  % (case_no+1, solution) 