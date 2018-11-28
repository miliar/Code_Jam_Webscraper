#!/usr/bin/env python
#coding:utf-8
# Author:  cmaske --<>
# Purpose: 
# Created: 3/9/2009

import sys
import re


#----------------------------------------------------------------------
def main(args):
    """Main"""
    f = open('A-large.in').readlines()
    L, D, N = unpack(f[0])
    words = load_words(f[1:D+1])
    counter = 0
    out = open('result-large.out','w')
    for expression in load_expressions(f[D+1:(D+1)+N+1]):
        counter += 1
        r = re.compile(expression)
        m = filter(lambda x: r.match(x), words)
        out.write('Case #%d: %d' % (counter, len(m))+'\n')
    out.close()
    
#----------------------------------------------------------------------
def unpack(s):
    """Function to unpack initial values"""
    return tuple([int(x) for x in s.split(' ')])

#----------------------------------------------------------------------
def load_words(words):
    """Return the possible words"""
    return [w.replace('\n','') for w in words]
    
#----------------------------------------------------------------------
def load_expressions(expressions):
    """Return the list that contains all expressions to compare"""
    for i in expressions:
        yield i.replace('(','[').replace(')',']').replace('\n','')

if __name__=='__main__':
    main(sys.argv)