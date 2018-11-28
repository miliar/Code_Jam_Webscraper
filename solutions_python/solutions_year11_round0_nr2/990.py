#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

def solve_case(combinations, oppositions, invocation):
    """
    combinations - lista trójek liter, pierwsze dwie robią trzecią
    oppositions - lista par liter, wiadomo
    invocation - jeden string
    """

    def combi_key(letter1, letter2):
        return "".join(sorted(letter1 + letter2))

    # para liter kombinacji -> efekt, para liter alfabetycznie
    combi = dict()
    for c in combinations:
        l1, l2, r = c
        combi[ combi_key(l1,l2) ] = r

    # litera -> zbiór jej opozycji
    oppo = defaultdict(lambda: set())
    for o in oppositions:
        l1, l2 = o
        oppo[l1].add(l2)
        oppo[l2].add(l1)
    
    current_stack = []

    for i in invocation:
        if current_stack:
            g = combi.get(combi_key(current_stack[-1], i), None)
            if g is not None:
                current_stack[-1] = g
                continue
        if oppo[i].intersection(set(current_stack)):
            current_stack = []
            continue
        current_stack.append(i)

    return current_stack
    #return (combinations, oppositions, invocation)

def parse_case(case_line):
    items = case_line.replace("\n", "").split(" ")
    combi_count = int(items[0])
    combinations = items[1:1+combi_count]
    oppo_count = int(items[1+combi_count])
    oppositions = items[2+combi_count:2+combi_count+oppo_count]
    invocation = items[3+combi_count+oppo_count]
    return (combinations, oppositions, invocation)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = sys.argv[0].replace(".py", ".in")
    input = open(filename)
    outputname = filename.replace(".in",".out")
    output = open(outputname, "w")

    print "Converting %s to %s" % (filename, outputname)

    cases_count = int(input.readline())
    for case_no in xrange(1, cases_count+1):
        reply = solve_case(* parse_case(input.readline()))
        txt = "Case #%d: [%s]\n" % (
            case_no, ", ".join(reply))
        output.write(txt)
        print txt,

    output.close()
    input.close()
