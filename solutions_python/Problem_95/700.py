#! /usr/bin/env python

# Speaking in Tongues
# Code Jam 2012 Round 1 - Problem A
# Mark Sherman brazentone@gmail.com

import sys

# Dictionary for character lookup (googlese=key, english=value)
dict = {
    'y' : 'a',
    'n' : 'b',
    'f' : 'c',
    'i' : 'd',
    'c' : 'e',
    'w' : 'f',
    'l' : 'g',
    'b' : 'h',
    'k' : 'i',
    'u' : 'j',
    'o' : 'k',
    'm' : 'l',
    'x' : 'm',
    's' : 'n',
    'e' : 'o',
    'v' : 'p',
    'z' : 'q',
    'p' : 'r',
    'd' : 's',
    'r' : 't',
    'j' : 'u',
    'g' : 'v',
    't' : 'w',
    'h' : 'x',
    'a' : 'y',
    'q' : 'z',
    ' ' : ' '   }

# Does the actual work solving the problem
def do_case(case_num):
    line = fin.readline()
    newline = translate(line[:-1])
    fout.write( "Case #" + str(case_num) + ": " + newline + '\n' )

def translate(line):
    if len(line) == 0 :
        return ''
    else:
        return dict[ line[0] ] + translate( line[1:] )

######################################################
# Setup stuff

OUTFILE = 'outfile'
    
fin = open(sys.argv[1], 'r')

fout = open(OUTFILE, 'w')

CASES = int(fin.readline()) 

for i in range(CASES):
    do_case(i+1)
    
    