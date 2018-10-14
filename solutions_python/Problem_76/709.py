#!/usr/bin/env python2.6

import sys
from itertools import chain, combinations

INPUT_FILE=file(sys.argv[1])
OUTPUT_FILE=file(sys.argv[1].replace('in', 'out'), 'w')
#OUTPUT_FILE=sys.stdout

def xor(sequence):
    sum_ = 0
    for elem in sequence:
        sum_ ^= elem
    return sum_


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def best_sum(candy_bag):
    candy_bag = map(int, candy_bag)
    
    max_sum = 0
    for i in powerset(candy_bag):
        j = [candy for candy in candy_bag]
        [j.remove(candy) for candy in i]
        if len(j) and len(i) and xor(j) == xor(i):
            s = sum(i)
            if s > max_sum:
                max_sum = s
            s = sum(j)
            if s > max_sum:
                max_sum = s

    return max_sum

def main():
    case_num = 1
    line = INPUT_FILE.readline() 
    while True:
        if not INPUT_FILE.readline():
            break

        line = INPUT_FILE.readline().strip()
        best_deal = best_sum(line.split(' '))

        if not best_deal:
            best_deal = 'NO'

        OUTPUT_FILE.write('Case #%s: %s\n' % (case_num, best_deal)) 
        case_num += 1

if __name__ == '__main__':
    main()
