#!/usr/bin/env python

from StringIO import StringIO
import sys

TEST_INPUT = '''5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW
'''

TEST_OUTPUT = '''Case #1: [E, A]
Case #2: [R, I, R]
Case #3: [F, D, T]
Case #4: [Z, E, R, A]
Case #5: []
'''

def pop(list):
    if len(list):
        list.pop()

def _frozenset(pair):
    '''Keep a set of two of the same elements from collapsing into one element'''
    if len(pair) != 2:
        return frozenset(pair)

    if pair[0] == pair[1]:
        return frozenset((pair[0], '-'))
    else:
        return frozenset(pair)

class Problem(object):
    def __init__(self, combinations, oppositions, elements):
        self.combinations = dict((_frozenset(c[:2]), c[2]) for c in combinations)
        self.oppositions = {}
        for o in oppositions:
            first, second = o
            self.oppositions.setdefault(first, []).append(second)
            self.oppositions.setdefault(second, []).append(first)
        self.elements = elements

    def solve(self):
        element_list = []
        for element in self.elements:
            element_list.append(element)
            last_two = _frozenset(element_list[-2:])
            if last_two in self.combinations:
                pop(element_list)
                pop(element_list)
                element_list.append(self.combinations[last_two])
            else:
                for opposing in self.oppositions.get(element, []):
                    if opposing in element_list:
                        element_list = []
        return element_list

def get_int(list):
    return int(list.pop(0))

def get_string(list):
    return list.pop(0)

def parse_line(line):
    components = line.split()

    number_of_combinations = get_int(components)
    combinations = []
    for i in xrange(number_of_combinations):
        combinations.append(get_string(components))

    number_of_oppositions = get_int(components)
    oppositions = []
    for i in xrange(number_of_oppositions):
        oppositions.append(get_string(components))

    number_of_elements = get_int(components)
    elements = get_string(components)

    return Problem(combinations, oppositions, elements)

def main(stdin, stdout):
    stdin.next()  # Skip the first line
    for i, line in enumerate(stdin, 1):
        problem = parse_line(line)
        element_list = problem.solve()
        stdout.write('Case #{0}: [{1}]\n'.format(i, ', '.join(element_list)))

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        output = StringIO()
        main(StringIO(TEST_INPUT), output)
        output.seek(0)
        output = output.read()
        assert output == TEST_OUTPUT, '{0} != {1}'.format(output, TEST_OUTPUT)
        print "OK"
    else:
        main(sys.stdin, sys.stdout)
