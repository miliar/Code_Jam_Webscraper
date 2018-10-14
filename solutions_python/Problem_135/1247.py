#!/usr/bin/python3

#$Id:$

# Google code jam 2014
# problem 1

import time
import getopt
import sys

def print_timing(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        print ('%s took %0.2f s' % (func.__name__, (t2-t1)))
        return res
    return wrapper

def usage():
    print('''
    Magic trick (task 1)

Options:
-h (--help) 
-v (--verbose)
''')


if __name__ == "__main__":

    verbose = False

    if sys.version_info[0] < 3:
        print("This script requires Python 3. (You are running %d.%d)" % (
            sys.version_info[0], sys.version_info[1])) 
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv",
                                   ["verbose","help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print (str(err)) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-v", "--verbose"):
            verbose=True
        else:
            usage()
            sys.exit()


    # reading input
    # first line: number of test cases. T cases follow
    # each test case:
    # integer (answer to first question)
    # next 4 lines: arrangement of the 16 cards
    # integer (answer to second question)
    # next 4 lines: arrangement of the 16 cards
    # example:
    # 1 
    # 2
    # 1 2 3 4
    # 5 6 7 8
    # 9 10 11 12
    # 13 14 15 16
    # 3
    # 1 2 5 4
    # 3 11 6 15
    # 9 10 7 12
    # 13 14 8 16
            
    fname = "input.txt"

    f = open(fname, "rt")
    ncases = int(f.readline())
    if verbose:
        print("%s: %d cases." % (fname, ncases))

    for c in range(ncases):
        s1 = set()
        s2 = set()

        a1 = int(f.readline())
        for r in range(4):
            l = f.readline()
            if r == a1 - 1:
                for item in l.split():
                    s1.add(item)
        a2 = int(f.readline())
        for r in range(4):
            l = f.readline()
            if r == a2 - 1:
                for item in l.split():
                    s2.add(item)

        if verbose:
            print("Case %d. Answers: %d %d" % (c, a1,a2))

        # solve it: read selected rows, create intersection
        # if 1 member -> solved
        # if empty: volunteer cheated
        # if multiple: bad magician

        intersect = s1.intersection(s2)

        if verbose:
            print (s1)
            print (s2)
            print(intersect)        

        # output
        if len(intersect) == 0:
            ostr = 'Volunteer cheated!'
        elif len(intersect) == 1:
            ostr = intersect.pop()
        else:
            ostr = 'Bad magician!'

        print ("Case #%d: %s" % (c+1, ostr))

        

        




