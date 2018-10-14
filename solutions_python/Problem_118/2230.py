#! /usr/bin/python

import sys
import math

def isPalin(num):
    strNum = str(num)
    if strNum == strNum[::-1]:
        #print '{0} is a palindrome'.format(strNum)
        return True
    else:
        #print '{0} is not a palindrome'.format(strNum)
        return False


def algo(filename):
    try:
        infile = open(filename+'.in', 'r')
        outfile = open(filename+'.out', 'w')
    except IOError:
        return

    T = int(infile.readline().strip())

    for case in range(1, T+1):

        A, B = [int(item) for item in infile.readline().strip().split(' ')]

        count = 0
        for i in range(A, B+1):
            if isPalin(i) == True:
                root = int(math.sqrt(i))
                #print "root = {0}".format(root)
                #print "floor = {0}".format(math.floor(root))

                if math.pow(root, 2) == i \
                        and isPalin(root) == True:
                            count = count + 1

        print "Case #{0}: {1}".format(case, count)
        outfile.write("Case #{0}: {1}\n".format(case, count))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        algo(sys.argv[1])
    else:
        print "no input"

    #isPalin(11)
    #isPalin(12321)
    #isPalin(1231)



