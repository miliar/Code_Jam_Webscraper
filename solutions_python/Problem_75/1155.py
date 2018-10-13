#!/usr/bin/python

from collections import defaultdict
import sys

def parse_case(case):
    elts = case.split()
    num_combines = int(elts[0])
    combines = elts[1:num_combines + 1]
    num_opposed = int(elts[num_combines + 1])
    opposed = elts[num_combines + 2:num_combines + num_opposed + 2]
    invokes = elts[-1]

    combine_pairs = defaultdict(set)
    combine_results = defaultdict(dict)
    for c1, c2, r in combines:
        combine_pairs[c1].add(c2)
        combine_pairs[c2].add(c1)
        combine_results[c1][c2] = r
        combine_results[c2][c1] = r

    opposed_pairs = defaultdict(set)
    for [o1, o2] in opposed:
        opposed_pairs[o1].add(o2)
        opposed_pairs[o2].add(o1)

    return (
        combine_pairs,
        combine_results,
        opposed_pairs,
        invokes
        )

def parse(file):
    file.readline()
    return [parse_case(case) for case in file]

def invoke_result(combine_pairs, combine_results, opposed_pairs, invokes):
    result = []
    for i in invokes:
        if not result:
            result = [i]
            continue
        else:
            last = result[-1]
            if last in combine_pairs[i]:
                result.pop()
                after_com = combine_results[i][last]
            else:
                after_com = i
            wipe = False
            for r in result:
                if after_com in opposed_pairs[r]:
                    result = []
                    wipe = True
                    break
            if not wipe:
                result.append(after_com)
    return result

def unparse(n, result):
    start = 'Case #{0}: ['.format(n)
    middle = ''.join('{0}, '.format(c) for c in result[:-1])
    if len(result) > 0:
        end = '{0}]'.format(result[-1])
    else:
        end = ']'
    string = start + middle + end
    print(string)

def main():
    with open(sys.argv[1]) as file:
        cases = parse(file)
        [unparse(n, invoke_result(*case)) for (n, case) in
         enumerate(cases, start=1)]

main()
