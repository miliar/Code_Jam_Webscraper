'''
Created on 13/04/13
Code Jam 2013 Qualification Round C
@author: manolo
'''
import math
import sys
ifile = sys.stdin
def r():
    return ifile.readline()[:-1]

ofile = open('./c-large1.out', 'w')
def w(what):
    ofile.write(what + '\n')

def is_fair(n):
    return str(n) == str(n)[::-1]

#def is_square(n):
#    sqrt = math.sqrt(n)
##    print 'sqrt = ' + str(sqrt)
#    if sqrt - long(sqrt) > 0:
#        return False
#    else:
#        return is_fair(long(sqrt))
    

def find(a, b):
    count = 0
#    print '(' + str(a) + ', ' + str(b) + ')'

    sqrt_a = math.sqrt(a)
#    print "sqrt_a: " + str(sqrt_a)
    long_sqrt_a = long(sqrt_a)
#    print "long_sqrt_a: " + str(long_sqrt_a)
    i = long_sqrt_a
    if sqrt_a - long_sqrt_a > 0:
        i += 1
#    print "i: " + str(i)

    bb = long(math.sqrt(b))
#    print '(' + str(i) + ', ' + str(bb) + ')'
    while (i <= bb):
        if is_fair(i):
            ii = i*i
            if is_fair(ii):
#                print ii
                count += 1
#        else:
#            print str(i) + " --> NO"
        i +=1
    return count

t = long(r())
#print 't: ' + str(t)

for i in xrange(t):
    (A, B) = r().split(' ')
    a = long(A)
    b = long(B)
    n = find(a, b)
    w('Case #' + str(i+1) + ': ' + str(n))

ofile.close

