#!/usr/bin/python2
"""
use arrays to check which cards are possibilities.
"""

import sys

def main(name):
    f = open(name, 'r')
    o = open("output.out", 'w')

    #get number of cases
    num_cases = int(f.readline())
    print num_cases, "here are num_cases"

    for i in range(num_cases):
        first_row = int(f.readline())
        print first_row, "here are first_row"

        a = []
        count = [0 for x in range(16)]
        for j in range(4):
            a.append(f.readline().split())
        
        for j in a[first_row-1]:
            count[int(j)-1] += 1

        print "here is count", count

        second_row = int(f.readline())
        print second_row, "here is second_row"

        b = []
        for j in range(4):
            b.append(f.readline().split())

        for j in b[second_row-1]:
            count[int(j) -1] += 1

        print "Here is count", count

        o.write("Case #" + str(i + 1) + ": " + get_output(count) + "\n")

    o.close()

def get_output(a):
    num_twos = 0
    last_two = -1

    for i in range(len( a)):
        if a[i] == 2:
            num_twos += 1
            last_two = i

    print "we encountered", num_twos, "number of twos"

    if num_twos == 1:
        return str(last_two + 1)
    elif num_twos > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"

main(sys.argv[-1])
