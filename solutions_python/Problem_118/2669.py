#
# Code by Fernando Gil <http://www.fernandogil.com.br> for Google Code Jam 2013
#
# Use:
# $python tictactoe.py sample.in
#
#
import math
import sys

def fair(n):
    n1 = list(str('%d' % n))
    n2 = list(str('%d' % n))
    n2.reverse()
    return n1 == n2

def calc(case,a,b):
    sqrtA = math.floor(math.sqrt(a))
    sqrtB = math.sqrt(b)
    i = a
    sqrtI = sqrtA

    #print "A = " + str(a)
    #print "B = " + str(b)
    #print "sqrtA = " + str(sqrtA)
    #print "sqrtB = " + str(sqrtB)

    found = 0
    while sqrtI <= sqrtB:
        if(fair(sqrtI)):
            square = math.pow(sqrtI,2)
            if(fair(square)):
                #print "%d^2 = %d" % (sqrtI,square)
                if(square >= a and square <= b):
                    found = found + 1
        sqrtI = sqrtI + 1
        
    print "Case #%d: %d" % (case,found)
    
# MAIN

filename = sys.argv[1]
file = open(filename, 'r')

cases = int(file.readline()) # cases line

case = 1
while case <= cases:
    line = file.readline().split(' ')
    a = int(line[0])
    b = int(line[1])
    calc(case,a,b)
    case = case + 1
    