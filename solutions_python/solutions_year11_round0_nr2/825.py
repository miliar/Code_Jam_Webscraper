#!/usr/bin/env python

import argparse

def main():
    parser = argparse.ArgumentParser(description="A. Bot Trust")
    parser.add_argument("filename")
    parser.add_argument("--pudb", action="store_true")
    args = parser.parse_args()

    if args.pudb:
        import pudb
        pudb.set_trace()

    f = open(args.filename)
    s = f.readlines()
    f.close()

    # number of test cases
    t = int(s[0])
    cases = {}
    for i in range(1, len(s)):
        cases[i] = s[i].replace('\n','')
    for i in sorted(cases.keys()):
        print "Case #{0}: {1}".format(i, solve(cases[i].split(' ')))

def solve(case):
    # number of combos
    c = int(case[0])
    case = case[1:]
    combos = []
    for i in range(c):
        combos.append(case[0])
        case = case[1:]
    # number of opposers
    d = int(case[0])
    case = case[1:]
    opposers = []
    for i in range(d):
        opposers.append(case[0])
        case = case[1:]
    # length of element chain
    n = case[0]
    case = case[1:]
    chain = case[0]
    result = []
    for element in chain:
        if len(result) == 0:
            result = [element]
            continue
        x = combo(element, combos, result)
        if x:
            result[-1] = x
        elif negates(element, opposers, result):
            result = []
        else:
            result.append(element)
    return convert(result)

def convert(result):
    a = '['
    l = len(result)
    for i,r in enumerate(result):
        a += r
        if i != l - 1:
            a += ', '
    a += ']'
    return a

def combo(element, combos, result):
    for c in combos:
        if element == c[0] and result[-1] == c[1]:
            return c[2]
        elif element == c[1] and result[-1] == c[0]:
            return c[2]

def negates(element, opposers, result):
    for o in opposers:
        if element in o:
            for r in result:
                if r in o and r != element:
                    return True
    return False

if __name__=="__main__":
    main()
