# python 3
import string
import itertools
import sys

def process_case(orig_nums):
    nums = orig_nums[:]
    distinct_ascending = list(set(nums))
    distinct_ascending.sort()
    result = 0
    for a in distinct_ascending:
        for i in range(len(nums)):
            while i<len(nums) and nums[-1-i] == a:
                del nums[-1-i]
                result += i
            while i<len(nums) and nums[i] == a:
                del nums[i]
                result += i
    return result

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        N = int(next(lines))
        nums = line_of_numbers(next(lines))
        result = process_case(nums)
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

##start('B-test')
##start('B-small-attempt0')
start('B-large')
