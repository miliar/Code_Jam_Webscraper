from fractions import gcd
from math import floor, log

def parse(name):
    in_file = open('%s.in' % name, 'r')
    cases = int(in_file.readline())
    lines = []
    for case in range(cases):
        p, q = in_file.readline().split('/')
        solution = solve(int(p), int(q))
        line = 'Case #%s: %s' % (case + 1, solution)
        print line
        lines.append(line)
    in_file.close()
    out_file = open('%s.out' % name, 'w')
    out_file.write('\n'.join(lines))
    out_file.close()

def solve(p, q):
    gcd_pq = gcd(p, q)
    p = p / gcd_pq
    q = q / gcd_pq
    return int(log(q, 2) - floor(log(p, 2))) if bin(q)[2:].count('1') == 1 else 'impossible'

parse('A-small-attempt0')
