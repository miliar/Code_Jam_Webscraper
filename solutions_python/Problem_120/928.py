'''
Created on 27/04/13
Code Jam 2013 Round 1A - A
@author: manolo
'''

import sys
from math import pi
ifile = sys.stdin
ofile = open('./a-small.out', 'w')

def read():
    return ifile.readline()[:-1]
    
def w(what):
#    print what
    ofile.write(what + '\n')

def area(radio):
    return pi * radio * radio


T = int(read())
#print str(T) + ' cases'
for i in range(1,T+1):
    (r, t) = read().split(' ')
    r = int(r)
    t = int(t)
#    print 'r = ' + str(r)
#    print 't = ' + str(t)
    r += 1
    milimeters = 2 * r - 1 # r*r - (r-1)*(r-1)
#    print 'mililiters needed for the first ring: ' + str(milimeters)
    
    n_circles = 0

    while (t >= milimeters):
        t = t - milimeters
#        print 't = ' + str(t)
        n_circles += 1
        r += 2
        milimeters = 2 * r - 1 # r*r - (r-1)*(r-1)
#        print 'mililiters needed for the ring: ' + str(milimeters)
    
    if n_circles < 1:
        n_circles = 1
        
    w('Case #' + str(i) + ': ' + str(n_circles))
#    sys.stdout.write('.')
    




ofile.close

