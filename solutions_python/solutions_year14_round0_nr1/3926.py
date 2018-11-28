#!/usr/bin/python
#
# Problem: Elegant Diamond
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 
# Comments: Might take a while. Try using pypy for faster results.

     
import sys
input = file(sys.argv[1])

def solve(s, p, ti):
    return True

for case in range(int(input.readline())):
    first_position = input.readline().split()
    first_position = int(first_position[0])

    a     = []
    list1 = input.readline().split()
    list2 = input.readline().split()
    list3 = input.readline().split()
    list4 = input.readline().split()
    a     = [list1, list2, list3, list4]

    # second position
    second_position = input.readline().split()
    second_position = int(second_position[0])
    b     = []
    list1 = input.readline().split()
    list2 = input.readline().split()
    list3 = input.readline().split()
    list4 = input.readline().split()
    b     = [list1, list2, list3, list4]

    c = [val for val in a[first_position - 1] if val in b[second_position - 1]]
    if len(c) > 0:
        if len(c) == 1:
            print "Case #%d: %d" % (case+1, int(c[0]))
        else:
            print "Case #%d: Bad magician!" % (case+1)
    else:
        print "Case #%d: Volunteer cheated!" % (case+1)
