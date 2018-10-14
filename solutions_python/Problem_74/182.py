# python 3
import string
import itertools
import sys

def process_case(plan):
    timeB = 0
    posB = 1
    timeO = 0
    posO = 1
    t = 0
    for (robot, button) in plan:
        if robot=='B':
            t = max(timeB + abs(posB - button) + 1,
                    t + 1)
            posB = button
            timeB = t
        else:
            t = max(timeO + abs(posO - button) + 1,
                    t + 1)
            posO = button
            timeO = t
    result = max(timeB, timeO)
    return result

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        s = next(lines)
        tab = s.split()
        plan = []
        for i in range(1,len(tab),2):
            plan.append( (tab[i], int(tab[i+1]) ))
        result = process_case(plan)
        yield 'Case #{0}: {1}\n'.format(ci, result)
    
def line_of_numbers(s):
    return [int(sub) for sub in s.split()]

def input_gen(f_in):
    for line in f_in:
        if line.endswith('\n'):
            line = line[:-1]
        yield line

def start(basename):
    infile = basename + '.in'
    outfile = basename + '.out'
    f_in = open(infile, 'r')
    f_out = open(outfile, 'w')
    f_out.writelines(result_gen(input_gen(f_in)))
    f_in.close()
    f_out.close()

##start('A-test')
##start('A-small-attempt0')
start('A-large')
