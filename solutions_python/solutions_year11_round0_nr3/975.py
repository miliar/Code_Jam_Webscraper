import numbers
from re import split, compile
import re
from random import randint
from string import ljust,rjust
from sys import argv

def run_file():
    if len(argv)>1:
        filename = argv[1]
    else:
        filename = 'A-large.in'
        filename = 'A-small.in'
    f=file(filename)
    program = f.readlines()
    f.close()
    line_no = 0
    case_no = 0
    first_line = str(program[0]).rstrip().split(' ')
    cases_no = int(first_line[0])

    line_no += 1
    patterns = []
    while case_no < cases_no:
        n = int(program[line_no].rstrip())
        line_no += 1
        case = program[line_no].rstrip()
        line_no += 1
        case_no += 1
        print "Case #" + str(case_no) + ": " + str(analyze(case, n))


def advance_one(pattern, n):
    i = 0
    while(i<n):
        if (pattern[i]==0):
            pattern[i]=1
            break
        else:
            pattern[i]=0
            i+=1


def sum_check(case, pattern, n):
    pat0 = 0
    sean0 = 0
    pat1 = 0
    sean1 = 0
    i = 0
    while(i<n):
        if (pattern[i]==0):
            pat0 ^= case[i]
            sean0 += case[i]
        else:
            pat1 ^= case[i]
            sean1 += case[i]
        i+=1
    if (pat0==pat1):
        return max(sean0, sean1)
    return 0


def analyze(case, n):
    pattern = []
    numbers_split=case.rstrip().split(' ')
    numbers =[]
    for number in numbers_split:
        numbers.append(int(number))
    actual_max=0
    pattern.append(1)
    for i in range(1, n):
        pattern.append(0)
    while(pattern.count(0)>0):
        sum = sum_check(numbers, pattern, n)
        if (sum>actual_max):
            actual_max=sum
        advance_one(pattern, n)
#        print pattern
    if (actual_max>0):
        return actual_max
    else:
        return "NO"


run_file()