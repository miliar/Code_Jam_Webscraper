#! /usr/bin/python

import re

def split(line):
    return chomp(line).split(' ')

def chomp(line):
    return line.replace('\n', '')

key = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
regex = re.compile('[a-z]')

def solve(case):
    answer = regex.sub(lambda m: key[m.group()], case)
    return "%s" % (answer)

if __name__ == '__main__':

    input_problem = 'A'
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
