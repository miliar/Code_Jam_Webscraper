#!/usr/bin/env python
#coding: UTF-8
'''
Solution for the 'Magic Trick' problem of Google Code Jam 2014

Copyright (c) 2014 Samuel Groß
'''

INPUTFILE  = "/home/sam/Desktop/small.in"
OUTPUTFILE = "/home/sam/Desktop/small.out"


def solve(row1, layout1, row2, layout2):
    res = layout1[row1 - 1] & layout2[row2 - 1]
    if len(res) == 1:
        return str(res.pop())
    elif len(res) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"


if __name__ == '__main__':
    infile  = open(INPUTFILE, 'r')
    outfile = open(OUTPUTFILE, 'w')

    testcases = int(infile.readline())
    counter   = 1


    for i in range(testcases):
        input = []
        row1 = int(infile.readline())
        layout1 = [ set(map(int, infile.readline().strip().split(' '))) for i in range(4) ]
        row2 = int(infile.readline())
        layout2 = [ set(map(int, infile.readline().strip().split(' '))) for i in range(4) ]

        sol = solve(row1, layout1, row2, layout2)	
        print("[*] Case %i solved, %.2f%% done" % (counter, float(counter) * 100 / testcases))
        outfile.write("Case #%i: %s\n" % (counter, sol))
        counter += 1

