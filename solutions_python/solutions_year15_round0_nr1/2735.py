#!env python

import sys

def solve(line):
    shyness_counts = map(int, line.split()[1])

    audience = 0
    for shyness, people in enumerate(shyness_counts):
        audience += people + max(shyness - audience, 0)
    return max(audience - sum(shyness_counts), 0)


if __name__=='__main__':
  sys.stdin.next()
  for case, line in enumerate(sys.stdin):
    print 'Case #{}: {}'.format(case+1, solve(line[:-1]))
