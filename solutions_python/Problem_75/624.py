#!/usr/bin/env python
#

import re
import sys
import os
import math

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
            f.write('Case #{0}: [{1}]\n'.format(i+1, ', '.join(self.results[i])))
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
        
        c = int(case[0])
        combinations = case[1:c+1]
        
        o = int(case[c+1])
        opossitions = case[c+2:c+o+2]
        
        m = int(case[c+o+2])
        magic = ''.join(case[c+o+3:c+o+m+3])
        
        magiclist = ''
        index = 0
        for i in range(0, len(magic)):
            magiclist += magic[i]
            
            print magiclist
            
            for comb in combinations:
                print magiclist, comb
                if magiclist.endswith(comb[0]+comb[1]):
                    magiclist = re.sub(r'{0}{1}$'.format(comb[0], comb[1]), comb[2], magiclist)
                    index = i + 1
                elif magiclist.endswith(comb[1]+comb[0]):
                    magiclist = re.sub(r'{0}{1}$'.format(comb[1], comb[0]), comb[2], magiclist)
                    index = i + 1

            for opos in opossitions:
                print magiclist, opos
                if re.search(r'{0}.*{1}'.format(opos[0], opos[1]), magiclist) or \
                    re.search(r'{0}.*{1}'.format(opos[1], opos[0]), magiclist):
                    magiclist = ''
                    index = 0
                #if re.search(r'{0}.*{1}'.format(opos[0], opos[1]), magiclist[index:]):
                #    magiclist = re.sub(r'{0}.*{1}'.format(opos[0], opos[1]), '', magiclist)
                #    index = len(magiclist) - 1
                #elif re.search(r'{0}.*{1}'.format(opos[1], opos[0]), magiclist[index:]):
                #    magiclist = re.sub(r'{0}.*{1}'.format(opos[1], opos[0]), '', magiclist)
                #    index = len(magiclist) - 1
            
        return list(magiclist)
                    

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