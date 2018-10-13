#!/usr/bin/env python

# Chuck norris gets reincarnated before he dies !

import sys
sys.setrecursionlimit(1000000) # this should be f*cking default parameter !

###############################################################################
#
#   The real stuff 
#
###############################################################################


def __gcd__(a,b):
    if b==0:
        return a
    return __gcd__(b,a%b)

def gcd(list):
    list.sort()
    g=list[0]
    for i in range(len(list)):
        g=__gcd__(g,list[i])
    return g

def __lcm__(a,b):
    l=a*b/__gcd__(a,b)
    return l

def lcm(list):
    list.sort()
    l=list[0]
    for i in range(len(list)):
        l=__lcm__(l,list[i])
    return l


def parse(f):
    n = int(f.readline().strip())
    for i in xrange(1,n+1):
        line = Line( f.readline().strip() ) 
        N = line.get_int()
        L = line.get_int()
        H = line.get_int()
        line = Line( f.readline().strip() ) 
        notes = line.get_int_list(N)
        solve(i, N, L, H, notes) 

def all_divide( low, note ):
    for n in low:
        if n==1 or note==1:
            continue
        if note % n != 0:
            return False
    return True
        

def all_multiple( high, note):
    for n in high:
        if n==1 or note==1:
            continue
        if n % note != 0:
            return False
    return True

def solve(case, N, L, H, notes):
    #print "intervalle= " + str([L, H]) + " notes = " + str(notes)
    if L<=1 and H>=1:
        print case_str(case) + "1" 
        return

    n = -1
    for i in xrange( L, H+1 ):
        low = [note for note in notes if note<=i]
        high = [note for note in notes if note >i]

        if all_divide(low, i) and all_multiple(high, i):
            n = i 
            break
    if n == -1:
        print case_str(case) + "NO" 
    else:
        print case_str(case) + str(n)

        
        


###############################################################################
#
#   Arg parsing helpers
#
###############################################################################

def case_str(n):
    return "Case #" + str(n) + ": "

# object to quickly get stuff from a input line
class Line(object):
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

def handle_input(ifile):
    f = open(ifile) 
    parse(f)
    f.close()

# main code
if len(sys.argv) < 2:
    print "You may want to give me an input file, jackass ?"
    sys.exit(1)
handle_input(sys.argv[1])

