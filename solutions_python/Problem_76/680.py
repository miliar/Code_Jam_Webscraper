#!/usr/bin/env python

from operator import xor

def xor_list(nums):
    result = 0
    for elem in nums:
        result = xor(result, elem)
    return result

def candy_split(candy):
    if xor_list(candy) != 0:
        return 'NO'
    else:
        cancopy = candy[:]
        mincan = min(cancopy)
        cancopy.remove(mincan)
        return sum(cancopy)

def process_input(inp):
    processed = inp.split()
    return map(int, processed)

def main():
    cases = input()
    results = []
    for case in range(cases):
        meaningless = input()
        inp = raw_input()
        candy = process_input(inp)
        results.append(candy_split(candy))
    for case in range(cases):
        print 'Case #' + str(case + 1) + ': ' + str(results[case])

if __name__ == '__main__':
    main()
