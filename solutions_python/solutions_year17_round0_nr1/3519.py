#!/usr/bin/env python3
import sys


"""
---+-++- 3
++++++++

++-+- 4


"""

def parse_test_file(filename):
    tc_list = []
    with open(filename) as f:
        t = next(f)
        for l in f:
            s, k = l.split()
            k = int(k)
            tc_list.append((s, k))
    return tc_list

def flip(x):
    if x == '-':
        return '+'
    else:
        return '-'

def process(s, k):
    s = list(s)
    flipcount = 0
    for i in range(len(s)):
        if s[i] == '-':
            try:
                for ik in range(k):
                    s[i+ik] = flip(s[i+ik])
            except IndexError:
                return -1
            flipcount += 1
    
    assert all(_ == '+' for _ in s)
    return flipcount





def output_results(results, file=sys.stdout):
    for i, result in enumerate(results):
        if result == -1:
            result = 'IMPOSSIBLE'
        print(f"Case #{i+1}: {result}", file=file)



def main(tc_list):    
    results = []
    for tc in tc_list:
        results.append(process(*tc))

    output_results(results)



if __name__ == '__main__':
    filename = sys.argv[1]
    tc_list = parse_test_file(filename)
    main(tc_list)