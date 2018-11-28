from sys import stdin
import re

T = int(stdin.readline())

for i in xrange(1, T+1):
    A1 = int(stdin.readline()) - 1
    lines = [map(int, stdin.readline().split()) for _ in xrange(4)]
    #row_1 = [_[A1] for _ in lines]
    row_1 = lines[A1]
    A2 = int(stdin.readline()) - 1
    lines = [map(int, stdin.readline().split()) for _ in xrange(4)]
    #row_2 = [_[A2] for _ in lines]
    row_2 = lines[A2]
    pfft = set(row_1) & set(row_2)
    if len(pfft) == 1:
        print "Case #{0}: {1}".format(i,list(pfft)[0])
    elif len(pfft) == 0:
        print "Case #{0}: Volunteer cheated!".format(i)
    else:
        print "Case #{0}: Bad magician!".format(i)
