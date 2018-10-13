
import csv
import itertools
import copy
import time
import numpy


def read_file(filename):
    f = open(filename)
    csv_r = csv.reader(f, delimiter=' ')
    T = int(csv_r.next()[0])
    test_lst = []
    for i in xrange(T):
        R, C, W = [int(e) for e in csv_r.next()]
        test_lst.append([R, C, W])
    f.close() 
    return test_lst 


def solve(R, C, W):
    if C-W > W:
        #print "coucou", R, C, W
        return 1+solve(R, C-W, W)
    else:
        return min(C, W+1)

def solve_test(test_case):
    R, C, W = test_case
    return solve(R, C, W)

def init():
    pass


def main(filename):
    test_lst = read_file(filename)
    init()
    for i_test, test_case in enumerate(test_lst):
        m1 = solve_test(test_case)
        print "Case #%i: %i" % (1+i_test, m1)


if __name__ == '__main__':
    #main('./simple.in')
    main('./A-small-attempt1.in')
    #main('./test.in')
    #main('./A-large.in')
    #main('./C-small-attempt2.in')

