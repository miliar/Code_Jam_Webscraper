#!/usr/bin/env python

import sys

def readline():
    return sys.stdin.readline().rstrip("\r\n")

def testcase():
    case_desc = iter(readline().split())

    C = int(case_desc.next())
    combinations = {}
    for i in xrange(C):
        a, b, c = case_desc.next()
        combinations[a+b] = c
        combinations[b+a] = c

    D = int(case_desc.next())
    opositions = {}
    for i in xrange(D):
        a, b = case_desc.next()
        opositions[a] = b
        opositions[b] = a

    N = int(case_desc.next())
    invoked = case_desc.next()
    assert len(invoked) == N
    result = ''
    for c in invoked:
        result += c
        combined = combinations.get(result[-2:])
        if combined is not None:
            result = result[:-2] + combined
        elif c in opositions and opositions[c] in result:
            result = ''
    return result

def main():
    n_cases = int(readline())
    for t_case in xrange(1, n_cases+1):
        print "Case #%d: [%s]" % (t_case, ', '.join(testcase()))

if __name__ == "__main__":
    main()

