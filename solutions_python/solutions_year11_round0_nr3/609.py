#!/usr/bin/env python
#

import itertools
import sys
import os

class Problem:
    cases = []
    results = []
    
    def __init__(self, filename):
        """
            Initialize the class, reading the test cases
            into the the self.cases property
        """
        self.filename = filename
        f = open(filename, 'r')
        input = [l[0:-1] for l in f]
        f.close()
        
        s = (len(input) - 1) / int(input[0])
        self.cases = [tuple(input[i:i+s]) for i in range(1, len(input), s)]
        #self.cases = map(lambda x: tuple(x.split(' ')), input[1:])

    def write(self):
        """
            Write the results in a new file
        """
        f = open('results-'+filename.split('/')[-1], 'w')
        for i in range(0, len(self.results)):
            f.write('Case #{0}: {1}\n'.format(i+1, ' '.join(self.results[i])))
        f.close()
        return self

    def resolve(self):
        """
            Iterate over the test cases and process a result
            for each case
        """
        self.results = [self.__process(case) for case in self.cases]
        return self
    
    def __process(self, case):
        """
            Process a test case and return and array with
            the solution.
        """
        d = [int(x) for x in case[1].split(' ')]
        d.sort()
        d.reverse()
        
        
        for i in range(len(d) - 1, 0, -1):
            for c in itertools.combinations(d, i):
                d2 = d[:]
                [d2.pop(d2.index(s)) for s in c]

                i = reduce(lambda x,y: x^y, c)
                j = reduce(lambda x,y: x+y, d2)
                f = reduce(lambda x,y: x+y, c)
                if i == j:
                    return [str(f)]
                
        return ['NO']

if __name__ == '__main__':
    # Check args
    if len(sys.argv) is not 2:
        print 'Usage: {0} input.txt'.format(sys.argv[0])
        exit(-1)
    
    filename = sys.argv[1]
    
    # Check if input file exists
    if not os.path.exists(filename):
        print 'Input file {0} doesn\'t exists'.format(filename)
        exit(-1)
    
    # Resolve the problem and write the results
    Problem(filename).resolve().write()