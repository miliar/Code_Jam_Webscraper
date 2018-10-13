import sys
from math import floor, ceil, sqrt
import pickle

def is_palindrome(x):
    return all( x[i] == x[-(i+1)] for i in xrange(len(x)>>1) )

def how_many(lb, ub):
    return len([1 for x in fair_and_square if x >= lb and x <= ub])

fair_and_square = []

# prelim
try:
    fas_dat = open('fair_and_square.dat', 'rb')
    fair_and_square = pickle.load(fas_dat)
except:
    N = 100000000
    for j in xrange(1,N):      
        if is_palindrome(str(j)):
            
            s = str(j**2)
            
            if is_palindrome(s):
                fair_and_square.append(int(s))
                print s, j

    fas_dat = open('fair_and_square.dat', 'wb')
    pickle.dump(fair_and_square,fas_dat)

#actual
with open(sys.argv[1]) as f:
    T = int(f.readline())
    for i,case in enumerate(f):
        lb, ub = map(int,case.split())
        print "Case #%d:" % (i+1), how_many(lb, ub)
