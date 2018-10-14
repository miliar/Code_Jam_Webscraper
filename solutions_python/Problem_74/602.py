#!/usr/bin/env python
#

import math
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
        
        #s = (len(input) - 1) / int(input[0])
        #self.cases = [tuple(input[i:i+s]) for i in range(1, len(input), s)]
        self.cases = map(lambda x: tuple(x.split(' ')), input[1:])

    def write(self):
        """
            Write the results in a new file
        """
        f = open('results-'+filename.split('/')[-1], 'w')
        for i in range(0, len(self.results)):
            f.write('Case #{0}: {1}\n'.format(i+1, ''.join(self.results[i])))
        f.close()
        return self

    def resolve(self):
        """
            Iterate over the test cases and process a result
            for each case
        """
        self.results = [self.__process(case) for case in self.cases]
        print self.results
        return self
    
    def __process(self, case):
        """
            Process a test case and return and array with
            the solution.
            
            
        """
        d={'O':1,'B':1}
        r=0
        for i in range(1, len(case) - 1, 2):
            (x,y) = (case[i], int(case[i+1]))
            
            a = max(y, d[x]) - min(y, d[x]) + 1
            r += a
            d[x] = y
            
            for j in range(i+2, len(case) - 1, 2):
                if x is not case[j]:
                    (n,m) = (case[j], int(case[j+1]))
                    if d[n] is not m:
                        if d[n] > m:
                            d[n] = max(d[n] - a, m)
                        else:
                            d[n] = min(d[n] + a, m)
                    break
        
        return [str(r)]
                    

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