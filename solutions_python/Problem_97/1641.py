#! /usr/bin/python

from collections import deque

def split(line):
    return chomp(line).split(' ')

def chomp(line):
    return line.replace('\n', '')

def shift(x, n = 1):
    d = deque(str(x))
    d.rotate(n)
    return int(''.join(d))

def solve(case):
    A, B = (int(i) for i in split(case))
#    print A, B
    seen = set()
    n = len(str(A))
    r = range(A, B+1)
    for i in r:
        for j in range(1, n):
            x = shift(i, j)
            if (x != i) and (x in r):
#                print '%s' % ((i, x),)
                seen.add((i, x))
    answer = len(seen) / 2
    return answer

if __name__ == '__main__':

    input_problem = 'C'
    input_set = 'small-attempt0'

    in_file = open('%s-%s.in' % (input_problem, input_set), 'r')
    out_file = open('%s-%s.out' % (input_problem, input_set), 'w')

    line = in_file.readline()

    count = int(line)
    print count, "cases"

    for i in range(1, count + 1):
        print i,
        case = chomp(in_file.readline())
        solution = solve(case)
        out_file.write('Case #%d: %s\n' % (i, solution))

    in_file.close()
    out_file.close()
