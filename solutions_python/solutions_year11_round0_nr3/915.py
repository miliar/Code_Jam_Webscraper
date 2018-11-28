#!/usr/bin/env python2

import itertools
import operator
import sys

def process(input_file):
    
    fd = open(input_file, 'r')

    num_tests = int(fd.readline())

    for i in xrange(1, num_tests+1):
        
        line = fd.readline()[:-1]
        print 'Case #%d:' %  i,

        candy_num = int(line)

        line = fd.readline()[:-1]
        
        candies = [ int(x) for x in line.split()]

        max_val = -1
        
        for j in xrange(1, len(candies)/2 + 1):

            for pile1 in itertools.combinations(candies, j):

                pile2 = candies[:]
                for e1 in pile1:
                    pile2.remove(e1)
                
                #print 'pile1', pile1, 'pile2', pile2

                real_val1 = reduce(operator.add, pile1)
                real_val2 = reduce(operator.add, pile2)
                
                bs_val1 = reduce(operator.xor, pile1)
                bs_val2 = reduce(operator.xor, pile2)

                if bs_val1 == bs_val2:
                    temp_max = max(real_val1, real_val2)
                    if temp_max > max_val:
                        max_val = temp_max

        if max_val == -1:
            print 'NO'
        else:
            print max_val

if __name__ == '__main__':
    
    #process('sample.in')
    process('small.in')

