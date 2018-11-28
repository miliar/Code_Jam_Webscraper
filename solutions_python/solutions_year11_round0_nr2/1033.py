#! /usr/bin/env python

import sys
from collections import defaultdict

if sys.stdin.isatty():
    # Open the file
    #reader = open('mini.in', 'r')
    reader = open('B-small-attempt3.in', 'r')
    #reader = open('B-large.in', 'r')


    for count, line in enumerate(reader):
        if count == 0:
            continue
        
        inputs = line.rstrip().split(" ")

        combine = defaultdict(dict)
        for x in range( 0, int(inputs.pop(0) )):
            elem = inputs.pop(0)
            combine[elem[0]][elem[1]] = elem[2]
            combine[elem[1]][elem[0]] = elem[2]
                        
        cancel = dict()
        for x in range( 0, int(inputs.pop(0) )):
            elem = inputs.pop(0)
            cancel[elem[0]] = elem[1]
            cancel[elem[1]] = elem[0]


        # Process the entries
        last = None
        killers = set()
        out = list()
        for elem in inputs[1]:
            # Check combine
            if last in combine:
                if elem in combine[last]:
                    out.pop()
                    out.append(combine[last][elem])
                    last = None
                    continue

            if last in cancel:
                killers.add( cancel[last] )
                
            # Check cancel
            if elem in killers:
                last = None
                out = list()
                killers = set()
                continue
            
            out.append(elem)
            last = elem
        out = '{0}'.format(out)
        print 'Case #{0}: {1}'.format(count, out.replace("'", ""))
