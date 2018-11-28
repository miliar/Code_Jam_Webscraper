#!/usr/bin/env python

import sys

if sys.stdin.isatty():

    sys.stderr.write('Please pipe in a file')
    sys.exit(1)

class Invoker(object):

    def __init__(self, combiners, opposers):

        self.combiners = dict()
        self.opposers = list()
        self.list = list()

        for combiner in combiners:
            char1, char2, result = combiner
            self.combiners[frozenset([char1, char2])] = result
            combiners = combiners[3:]

        
        for opposer in opposers:
            self.opposers.append(set(opposer))
            opposers = opposers[2:]

    def add_element(self, element):

        self.list.append(element)

        #if only one item, there's
        #nothing to do
        if len(self.list) == 1:
            return None

        #check for combiners
        last_two = frozenset(self.list[-2:])
        if last_two in self.combiners:
            self.list = self.list[:-2]
            self.list.append(self.combiners[last_two])

        #check for opposers
        if any([
            opp.issubset(self.list) 
            for opp in self.opposers
        ]):
            self.list = list()
    @property
    def elements(self):
        return '[' + ', '.join(self.list) + ']'

#read the first line which contains the
#number of tests
sys.stdin.next()

#process remaining records
case_number = 0

for line in sys.stdin:

    case_number += 1

    combiners = opposers = elements = ''

    values = line.strip().split()

    #get combiners
    num_combiners = int(values.pop(0))
    combiners = values[:num_combiners]
    values = values[num_combiners:]

    #get opposers
    num_opposers = int(values.pop(0))
    opposers = values[:num_opposers]
    values = values[num_opposers:]


    assert(len(values) == 2)
    elements = values[1]

    del(values)

    invoker = Invoker(combiners, opposers)
    for element in elements:
        invoker.add_element(element)

    print "Case #{num}: {elements}".format(
        num = case_number,
        elements = invoker.elements
    )

