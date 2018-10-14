#!/usr/bin/env python

def read_inputs():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        s = raw_input() # read a list of integers, 2 in this case
        print "Case #{}: {}".format(i, get_tidy_number(s))
        # check out .format's specification for more formatting options

def get_tidy_number(n):
    length = len(n)
    checkMore = True
    while checkMore:

        checkMore = False

        for i in xrange(0, (len(n) -1)):

            a = int(n[i])

            if len(n) <= i+1:
                #print "breaking .. len = %d, b = %d" % (len(n), i+1)
                break

            b = int(n[i+1])

            #print "a = %d, b = %d " % (a, b)

            if a > b:

                aNew = a
                if aNew == 0:
                     aNew = ''

                #print "aNew = %s " + str(aNew)

                size = (len(n)) - (i+1)
                nins = '9'*size

                #print "nines = %s " % nins
                #print nins

                tmpN = n[:i] + str(aNew)

                newA = int(tmpN) - 1

                #print "new a = %d " % newA

                n = str(newA) + nins
                checkMore = True
                #print n

    checkZeroPrefix = True

    index = 0
    while checkZeroPrefix:
        if n[index] == '0':
            n = n[index+1:]
        elif n[index] != '0':
            break

    return n



def main():
    read_inputs()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupting..'