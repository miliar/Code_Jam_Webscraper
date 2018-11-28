import string
import itertools
import sys
import fractions

def process_case(numbers):
    diffs = deltas(sorted(numbers))
    gcd = multi_gcd(diffs)
    result = (-numbers[0])%gcd
    return result

def deltas(numbers):
    return [numbers[i+1]-numbers[i]
            for i in range(len(numbers)-1)]

def multi_gcd(numbers):
    result = numbers[0]
    for x in numbers:
        result = fractions.gcd(result,x)
    return result

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        numbers = line_of_numbers(next(lines))[1:]
        result = process_case(numbers)
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

start('B-test')
