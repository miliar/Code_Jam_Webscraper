#!/usr/bin/python
#
# This script was written by Norio TAKEMOTO 2012-4-13

import re, sys
import numpy as np

###############################
#infile=open('input.dat', 'r')
infile=open('A-small-attempt0.in', 'r')
#infile=open('A-large-practice.in', 'r')
#outfile=open('output.dat', 'w')
outfile=open('A-small-attempt0.out', 'w')
#outfile=open('A-large-practice.out', 'w')
###############################


def convl_GtoE(lG):
    "convert a letter lG in Googlese to the corresponding letter lE in English"
   
    if lG==' ':
        return ' '

    if lG < 'n':

        if   lG=='a':
            return 'y'
        elif lG=='b':
            return 'h'
        elif lG=='c':
            return 'e'
        elif lG=='d':
            return 's'
        elif lG=='e':
            return 'o'
        if   lG=='f':
            return 'c'
        elif lG=='g':
            return 'v'
        elif lG=='h':
            return 'x'
        elif lG=='i':
            return 'd'
        elif lG=='j':
            return 'u'
        elif lG=='k':
            return 'i'
        elif lG=='l':
            return 'g'
        elif lG=='m':
            return 'l'

    else:

        if   lG=='n':
            return 'b'
        elif lG=='o':
            return 'k'
        elif lG=='p':
            return 'r'
        elif lG=='q':
            return 'z'
        if   lG=='r':
            return 't'
        elif lG=='s':
            return 'n'
        elif lG=='t':
            return 'w'
        elif lG=='u':
            return 'j'
        elif lG=='v':
            return 'p'
        elif lG=='w':
            return 'f'
        elif lG=='x':
            return 'm'
        elif lG=='y':
            return 'a'
        elif lG=='z':
            return 'q'

    return None


def solve_case(strG, jcase):

    outfile.write('Case #%i: '%(jcase+1))
    for lG in strG:
        outfile.write(convl_GtoE(lG))
    outfile.write('\n')
    


numcase = int(infile.readline())
for jcase in range(numcase):
    line = infile.readline()
    solve_case(line[0:len(line)-1], jcase)

outfile.close()
