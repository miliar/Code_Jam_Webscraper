#!/usr/bin/env python
"""
Module docstring
This serves as a long usage message.
"""
import sys
import re

T = int(sys.stdin.readline())
for j in range(T):
    line = sys.stdin.readline().split(" ")

    C = int(line.pop(0))
    combinators = {}
    for i in range(C):
        combinator = line.pop(0)
        combinators[combinator[0] + combinator[1]] = combinator[2]
        combinators[combinator[1] + combinator[0]] = combinator[2]

    D = int(line.pop(0))
    destructors = {}
    for i in range(D):
        destructor = line.pop(0)
        destructors[destructor[0] + destructor[1]] = True
        destructors[destructor[1] + destructor[0]] = True

    N = int(line.pop(0))
    elements_in = list(line.pop(0).rstrip())

    elements_out = []
    elements_out.append(elements_in.pop(0))

    for element in elements_in:
        if len(elements_out) == 0:
            elements_out.append(element)
            continue
        last_element = elements_out[-1]
        destructed = False
        if elements_out[-1] + element in combinators:
            elements_out.append(combinators[elements_out.pop(-1) + element])
        else:
            for a in elements_out:
                if a+element in destructors:
                    elements_out = []
                    destructed = True
                    break
            if not destructed:
                elements_out.append(element)


    print "Case #%d: [%s]" % (j + 1, ", ".join(elements_out)) 
