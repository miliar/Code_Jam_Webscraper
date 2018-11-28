#!/usr/bin/env python
# Google Code Jam 2011
# Qualification Round
# Problem B - Magicka
# May 7th 2011
# David Antliff <david.antliff@gmail.com>

import sys
import itertools

class TestCase(object):

    def __init__(self, combine_rules, oppose_rules, invoke_list):

        # store rules for fast lookup

        # combine rules will be applied to adjacent elements
        self.combine_rules = dict()
        for r in combine_rules:
            self.combine_rules[ (r[0], r[1]) ] = r[2]
            self.combine_rules[ (r[1], r[0]) ] = r[2]

        # oppose rules will be applied anywhere, after combine
        # keep a list of opposed elements for each element
        self.oppose_rules = dict()
        for r in oppose_rules:
            #self.oppose_rules[ r[0] ] = self.oppose_rules.get(r[0], []) + [r[1]]
            #self.oppose_rules[ r[1] ] = self.oppose_rules.get(r[1], []) + [r[0]]
            try:
                self.oppose_rules[ r[0] ].add(r[1])
            except KeyError:
                self.oppose_rules[ r[0] ] = set([r[1]])

            try:
                self.oppose_rules[ r[1] ].add(r[0])
            except KeyError:
                self.oppose_rules[ r[1] ] = set([r[0]])

        self.invoke_list = invoke_list

    def __str__(self):
        return """combine: %s
oppose: %s
invoke: %s
""" % (self.combine_rules, self.oppose_rules, self.invoke_list)


    def invoke_spells(self):

#        print self

        output = []

        # iterate through input
        for element in self.invoke_list:

            if not output:
                output.append(element)
                continue

            # first compare with last element
            if self.combine_rules.has_key( (output[-1], element) ):
                # combine
                non_base = self.combine_rules[ (output[-1], element) ]
#                print("combined %s with %s to create %s" % (output[-1], element, non_base))
                output.pop()
                output.append(non_base)
            else:
                output.append(element)

                if self.oppose_rules.has_key(element):
                    # search for an opposing element
                    opposing_elements = self.oppose_rules[element]
                    match = opposing_elements.intersection(set(output))
                    if match:
#                        print("oppose: %s with %s" % (element, match))
                        output = []

        return output


def main():

    #input = sys.stdin
    input = open(sys.argv[1], 'r')

    test_cases = []

    # read input file
    T = int(input.readline())  # number of cases

    for i in range(T):
        line = input.readline().split()

        # C - combine rules
        C = int(line.pop(0))
        if C:
            combine_rules = line[:C]
            line = line[C:]
        else:
            combine_rules = []

        # D - opposition rules
        D = int(line.pop(0))
        if D:
            oppose_rules = line[:D]
            line = line[D:]
        else:
            oppose_rules = []

        # N - input sequence
        N = int(line.pop(0))
        invoke_list = list(line.pop(0))

        assert(line == [])

        test_cases.append( TestCase(combine_rules, oppose_rules, invoke_list) )

    assert(len(test_cases) == T)

    # process test cases
    R = process_test_cases(test_cases)
    assert(len(R) == T)

    # print output file
    for i, r in enumerate(R):
        li = ", ".join(r)
        print("Case #%d: [%s]" % (i + 1, li))


def process_test_cases(test_cases):

    results = []
    num = len(test_cases)

    for i, case in enumerate(test_cases):
        sys.stderr.write("test case %d / %d\n" % (i + 1, num))
        r = case.invoke_spells()
        results.append(r)

    return results



if __name__ == "__main__":
    main()
