#!/usr/bin/python

import sys

def get_file(argv):
    if len(argv) == 1:
        return "a.txt"
    else:
        return "a_%s.txt" % (argv[1])

def print_answer(t, answer):
    print "Case #%d: %s" % (t, answer) 

def main(argv):
    filename = get_file(argv)
    f = open(filename, 'r')
    T = int(f.readline())
    for t in xrange(1, T+1):
        a = int(f.readline())
        for i in xrange(0,4):
            line = f.readline()
            if i == a-1:
                A = [int(temp) for temp in line.split(" ")]
        b = int(f.readline())
        for i in xrange(0,4):
            line = f.readline()
            if i == b-1:
                B = [int(temp) for temp in line.split(" ")] 
        same = set(A).intersection(B)
        if len(same) == 0:
            print_answer(t, "Volunteer cheated!")
        elif len(same) == 1:
            print_answer(t, same.pop())
        else:
            print_answer(t, "Bad magician!")


if __name__ == "__main__":
    main(sys.argv)