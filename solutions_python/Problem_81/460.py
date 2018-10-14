#!/usr/bin/env python

# Chuck norris gets reincarnated before he dies !

import sys
sys.setrecursionlimit(1000000) # this should be f*cking default parameter !

###############################################################################
#
#   The real stuff 
#
###############################################################################

def count_wp( line ):
    w = float(0)
    s = float(0)
    for i,c in enumerate(line):
        if c == '.':
            continue
        if c == '1': 
            w += 1            
            s += 1
            continue
        if c == '0':
            s += 1
            continue 
    return w/s


def count_wp( line, throw=-1 ):
    w = float(0)
    s = float(0)
    for i,c in enumerate(line):
        if i==throw:
            continue
        if c == '.':
            continue
        if c == '1': 
            w += 1            
            s += 1
            continue
        if c == '0':
            s += 1
            continue 
    #if( throw != -1 ):
    #    print "WP " + line + " throwing " + str(throw) + " = " + str(w/s)
    return w/s

def number_match( line ):
    s = 0
    for c in line:
        if c == '1' or c=='0': 
            s += 1
    #print "number match " + line + " = " + str(s)
    return s


def solve(score_lines):

    W = [float(0) for i in score_lines]
    OWP = [float(0) for i in score_lines]
    OOWP = [float(0) for i in score_lines]

    # calculate WP
    WP = [count_wp(score) for score in score_lines]  
    #print "WP=", WP

    # calculate OWP
    for i, score in enumerate(score_lines):
        for j,c in enumerate(score):
            if i==j :
                continue
            if c == '.':
                continue
            OWP[i] += count_wp(score_lines[j], i) 
        #print "OWP[" + str(i) + "] before divide = " + str(OWP[i])
        OWP[i] /= number_match(score)
    #print "OWP=", OWP




    # calculate OOWP
    for i, score in enumerate(score_lines):
        for j,c in enumerate(score):
            if c == '1' or c=='0': 
                OOWP[j] += OWP[i]
                continue
    # divide by the number of match played
    for i, score in enumerate(score_lines):
        OOWP[i] = OOWP[i] / number_match(score)

 

    #print "OOWP=", OOWP
    
    RPI = [0 for i in score]
    for i,score in enumerate(score_lines):
        RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]
    
    #print "RPI=", RPI
    for r in RPI:
        print r 



            


###############################################################################
#
#   Arg parsing
#
###############################################################################

# object to quickly get stuff from a input line
class Case(object):
    def __init__(self, line):
        self.line = line 
        self.line_split = line.split(" ")
        self.index = 0

    def get_str(self):
        s = str( self.line_split[self.index] )
        self.index += 1
        return s 

    def get_int(self):
        n = int( self.line_split[self.index] )
        self.index += 1
        return n

    def get_int_list(self, size=None):
        if size is None:
            # first number is the size of the list
            size = int( self.line_split[self.index] )
            self.index += 1
        l = [int(self.line_split[i]) for i in xrange(self.index, self.index + size)]
        self.index += size 
        return l

    def get_str_list(self, size=None):
        if size is None:
            # first number is the size of the list
            size = int( self.line_split[self.index] )
            self.index += 1
        l = [self.line_split[i] for i in xrange(self.index, self.index + size)]
        self.index += size 
        return l

def parse_and_solve_case(scores):
    return solve(scores) # call to solve !

def parse_and_solve(ifile):
    f = open(ifile) 
    n = int(f.readline().strip())
   
    for i in xrange(1,n+1):
        case = int(f.readline().strip())
        scores = []
        for j in xrange(0,case):
            scores.append( f.readline().strip() )
        print "Case #" + str(i) + ":"
        parse_and_solve_case(scores)

# main code
if len(sys.argv) < 2:
    print "You may want to give me an input file, jackass ?"
    sys.exit(1)
parse_and_solve(sys.argv[1])

