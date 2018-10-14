#!/usr/bin/env python
#By Jai Dhyani

import math, sys, os

def getints(f):
    return [int(x) for x in f.readline().split()]

num_surprises=0
def solve( x ):
    num_googlers=x[0]
    global num_surprises 
    num_surprises = x[1]
    p = x[2]
    totals=x[3:]
    def possible( total ):
        global num_surprises
        if total==0:
            return p==0
        if total>=28:
            return True
        if (total%3)==1:
            return p<=(total+2)/3
        else:
            if p<=(total+1)/3:
                return True
            elif p<=(total+4)/3 and num_surprises>0:
                num_surprises=num_surprises-1
                return True
        return False
    return sum([possible(t) for t in totals])

if __name__ == '__main__':
    filenames = [f for f in os.listdir('.') if f[-2:]=='in']
    for filename in filenames:
        outname=filename+'.out'
        f=open(filename)
        out=open(outname,'w')
        try:
            numtrials = getints(f)[0]
        except IndexError as ie:
            print 'no input data in %s'%filename
            exit(0)
        for i in xrange(numtrials):
            answer_num = solve(getints(f))
            answer_str = "Case #%d: %d"%(i+1,answer_num)
            print(answer_str)
            out.write(answer_str+'\n')
