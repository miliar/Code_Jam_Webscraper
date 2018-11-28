#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tung
#
# Created:     13/04/2013
# Copyright:   (c) Tung 2013
#-------------------------------------------------------------------------------

from math import *

palindrome_list = []

def find_palindrome():
    x = 0
    while(x <= 10000000):
        if(str(x) == str(x)[::-1] and str(x*x) == str(x*x)[::-1]):
            palindrome_list.append(x*x)
        x = x + 1
    pass

def main():
    try:
        f = open('C-large.in')
        try:
            o = open('C-large.out','w')
            i = 0
            for line in f:
                if(i>=1):
                    L = line.split(' ')
                    A = int(L[0])
                    B = int(L[1])
                    y = 0
                    for x in xrange(len(palindrome_list)):
                        if(palindrome_list[x] >= A and palindrome_list[x] <=B):
                            y = y + 1
                    print 'Case #' + str(i) + ':', y
                    print >>o, 'Case #' + str(i) + ':', y
                i = i + 1
        except IOError:
            print "Cant not create file"
    except IOError:
        print "File not found"
    pass

if __name__ == '__main__':
    find_palindrome()
    main()