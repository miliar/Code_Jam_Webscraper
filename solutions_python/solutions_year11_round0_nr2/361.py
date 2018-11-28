#!/usr/bin/python
import sys

def make_combines(sources):
    result = {}
    for source in sources:
        result[tuple(sorted(source[:2]))] = source[2]
    return result

def make_opposites(sources):
    result = {}
    for source in sources:
        result[tuple(sorted(source[:2]))] = True
    return result

def invoke(elements, combines, opposites):
    result = []
    for x in elements:
        result.append(x)
        combine_candidate = tuple(sorted(result[-2:]))
        if len(result) >= 2 and combine_candidate in combines:
            result.pop()
            result.pop()
            result.append(combines[combine_candidate])
            continue
        if len(result) >= 2:
            for i in xrange(len(result)-1):
                opposite_candidate = tuple(sorted((result[i], result[-1])))
                if opposite_candidate in opposites:
                    result = []
                    break
    return result

if __name__ == '__main__':
    num_cases = int(sys.stdin.readline().rstrip('\n'))
    for T in xrange(1, num_cases+1):
        test_case = sys.stdin.readline().split()
        num_combines = int(test_case[0])
        combines = make_combines(test_case[1:num_combines+1])
        num_opposites = int(test_case[num_combines+1])
        opposites = make_opposites(
                    test_case[num_combines+2:num_combines+num_opposites+2])
        elements = test_case[-1]
        result = invoke(elements, combines, opposites)
        result_str = '[' + ", ".join(result) + ']'
        print "Case #%d: %s" % (T, result_str)
