#!/usr/bin/python
'''
Google code jam 2015
Qualification Round
Infinite House of Pancakes

By Tyrus Tenneson
2015-04-11
'''

import sys

'''
Solution
'''

'''
def min_steps(plates, i=0):
    #print "whoa", i
    #print plates
    if sum(plates) == 0:
        print "DONEZO", i
        return 0
    let_eat = [max(0, x-1) for x in plates]
    # Don't move if largest is 1.
    if plates[-1] == 1:
        #print "DONEZO", i
        return i+1
    # Move half from largest plate.
    plates.append(plates[-1] / 2)
    plates[-2] = plates[-2] - plates[-1]
    special = sorted(plates)

    #print "s: ", special
    #print "l: ", let_eat
    return min(min_steps(let_eat, i+1), min_steps(special, i+1))
'''

mem = {}
def min_steps(plates):
    plates = sorted(plates)
    key = tuple(plates)
    if key in mem:
        return mem[key]
    if sum(plates) == 0:
        return 0
    bite = filter(lambda x: x > 0, [x - 1 for x in plates])
    largest = plates.pop()
    if largest == 1:
        return 1

    stuff = []
    for i in range(1, largest / 2 + 1):
        stuff.append(plates + [i, largest - i])
    mem[key] = min(map(min_steps, [bite] + stuff)) + 1
    return mem[key]

def eval_case(case):
    '''
    Returns solution to case
    '''
    D, plates = case
    return min_steps(plates)

'''
I/O
'''
def process_input():
    '''
    Reads stdin, returns cases ((D, (P_1, ...)), ...)
    '''
    with sys.stdin as input:
        num_cases = int(input.readline().rstrip())
        cases = []
        for x in range(num_cases):
            cases.append((int(input.readline()),
                          tuple(map(int, input.readline().split(' ')))))
        assert num_cases == len(cases)
    return tuple(cases)

def solve():
    cases = map(eval_case, process_input())
    for idx, val in enumerate(cases):
        write_string = "Case #%i: %s\n" % (idx+1, val)
        print write_string,

if __name__ == "__main__":
    solve()
