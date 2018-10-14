#!/usr/bin/python2.7

from collections import defaultdict
import sys

with open(sys.argv[1]) as input_file:
    input_file.readline()
    for case, line in enumerate(input_file):
        fields = line.split()

        nof_combinations = int(fields.pop(0))
        combinations = {}
        for _ in xrange(nof_combinations):
            spec = fields.pop(0)
            combinations[tuple(sorted(spec[:2]))] = spec[2]

        nof_opposed = int(fields.pop(0))
        opposed = defaultdict(list)
        for _ in xrange(nof_opposed):
            spec = fields.pop(0)
            opposed[spec[0]].append(spec[1])
            opposed[spec[1]].append(spec[0])

        fields.pop(0) # ignore the number of invocations

        element_list = []
        invocations = fields.pop(0)
        for invocation in invocations:
            element_list.append(invocation)
            if len(element_list) > 1:
                two = tuple(sorted(element_list[-2:]))
                if two in combinations:
                    element_list[-2:] = combinations[two]
                else:
                    for candidate in opposed[invocation]:
                        if candidate in element_list:
                            del element_list[:]

        answer = ', '.join(element_list)

        print "Case #%d: [%s]" % (case + 1, answer)
