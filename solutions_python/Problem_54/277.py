
#
# Google Code Jam 2010
# Qualification round: B. Fair Warning
# submission by EnTerr
#

import sys

f = open(sys.argv[1])
def input(): return f.readline().strip();

def GCD(lst):
    # calculate Greatest Common Divisor for list of natural numbers
    assert(len(lst)>0)
    while len(lst)>1:
        a = lst[0]
        lst = [ i % a for i in lst if i%a > 0 ]
        lst.append(a)
    return lst[0]


for caseNo in xrange(1, int(input())+1):
    T = map(int, input().split())[1:]
    gcd = GCD([i-j for i in T for j in T if i>j ])
    y = - T[0] % gcd
    print 'Case #%d: %s' % (caseNo, y)

