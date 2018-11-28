#!/usr/bin/env python

import sys
import select
import itertools

def make_case(line):
    # First an integer C, followed by C strings, each containing three
    # characters: two base elements followed by a non-base element. This
    # indicates that the two base elements combine to form the non-base
    # element. Next will come an integer D, followed by D strings, each
    # containing two characters: two base elements that are opposed to
    # each other. Finally there will be an integer N, followed by a
    # single string containing N characters: the series of base elements
    # you are to invoke. You will invoke them in the order they appear
    # in the string (leftmost character first, and so on).

    line = line.split()

    i = 0
    
    C = int(line[i])
    i += 1

    base = {}
    for c in xrange(C):
        s = line[i]
        i += 1
        base[s[0:2]] = base[s[1::-1]] = s[2]

    D = int(line[i])
    i += 1

    opposed = {}
    for d in xrange(D):
        for element, opposed_element in set(itertools.permutations(line[i])):
            try:
                opposed[element].add(opposed_element)
            except KeyError:
                opposed[element] = set((opposed_element,))
        i += 1

    N = int(line[i])
    i += 1
    invoked = list(line[i])[:N]

    return base, opposed, invoked


def test_result(case):
    base, opposed, invoked = case

    start, end = 0, 0
    result = invoked

    for i in xrange(len(invoked)):
        result[end] = invoked[i]
        end += 1
        if end - start >= 2:
            last2 = ''.join(result[end-2:end])
            if last2 in base:
                result[end-2] = base[last2]
                end -= 1
            elif result[end-1] in opposed and set(result[start:end]) & opposed[result[end-1]]:
                start = end
    
    return '[' + ', '.join(result[start:end]) + ']'
    

if __name__ == "__main__":
    
    try:
        try:
            data = open(sys.argv[1])
        except:
            data = sys.stdin
        if select.select([data,],[],[],0.0)[0]:
            lines = data.readlines()
        T = int(lines[0])
    except:
        sys.exit('Usage: %(file)s input-filename' % dict(file=__file__))

    for t in xrange(1, T+1):
        line = lines[t]
        result = test_result(make_case(line))
        print 'Case #%d: %s' % (t, result)
