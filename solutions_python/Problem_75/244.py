# -*- coding: utf-8 -*-

import sys

def parse_combines(combines):
    d = {}
    if combines:
        for c in combines:
            d[c[0] + c[1]] = c[2]
            d[c[1] + c[0]] = c[2]
    return d

def parse_opposites(opposits):
    d = {}
    if opposits:
        for o in opposits:
            d[o[1]] = o[0]
            d[o[0]] = o[1]
    return d

def solve_case(combines, opposits, elements):
    combines = parse_combines(combines)
    opposits = parse_opposites(opposits)
    elements_list = []
    for element in elements:
        if elements_list:
            last = elements_list[-1]
            if (last + element) in combines:
                elements_list[-1] = combines[last + element]
            else:
                opposit = opposits.get(element)
                if opposit and opposit in elements_list:
                    elements_list = []
                else:
                    elements_list.append(element)
        else:
            elements_list.append(element)
    return elements_list

def test():
    assert solve_case(None, None, 'EA') == ['E', 'A']
    assert solve_case(['QRI'], None, 'RRQR') == ['R', 'I', 'R']
    assert solve_case(['QFT'], ['QF'], 'FAQFDFQ') == ['F', 'D', 'T']
    assert solve_case(['EEZ'], ['QE'], 'QEEEERA') == ['Z', 'E', 'R', 'A']
    assert solve_case(None, ['QW'], 'QW') == []

    assert solve_case(['QRI', 'QFT'], None, 'FQFAQR') == ['T', 'F', 'A', 'I']
    assert solve_case(None, ['AS', 'DF'], 'ADFV') == ['V']

if __name__ == '__main__':

    test()

    if len(sys.argv) == 2:
        f = open(sys.argv[1])
        if f:
            n = f.readline()
            out = open("output", "w")
            idx = 1
            for line in f:
                items = line.strip().split()
                combines = []
                opposits = []
                elements = ''
                num = int(items.pop(0))
                while num > 0:
                    combines.append(items.pop(0))
                    num -= 1
                num = int(items.pop(0))
                while num > 0:
                    opposits.append(items.pop(0))
                    num -= 1
                elements = items.pop()

                r = solve_case(combines, opposits, elements)
                out.write("Case #%s: [%s]\n" % (idx, ', '.join(r)))

                idx += 1
        else:
            print 'Can not open file', sys.argv[1]
    else:
        print 'Invalid parameters number'
