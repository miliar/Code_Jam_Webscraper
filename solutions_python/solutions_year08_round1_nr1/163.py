#!/usr/bin/python

from sys import stdin
import gmpy

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

num = int(stdin.readline()[:-1])

for i in range(1, num + 1):
    stdin.readline()
    vector1 = stdin.readline()[:-1].split(" ")
    vector2 = stdin.readline()[:-1].split(" ")
    vector1 = [int(x) for x in vector1]
    vector2 = [int(x) for x in vector2]
    vector1 = sorted(vector1)
    vector2 = sorted(vector2, reverse=True)
#    lowest_sum = False
#    for p1 in all_perms(vector1):
#        for p2 in all_perms(vector2):
#            # print p1, p2
#            sum = 0
#            for (index, x) in enumerate(p1):
#                sum += int(x) * int(p2[index])
#            if lowest_sum == False or sum < lowest_sum:
#                lowest_sum = sum
    sum = gmpy.mpz(0)
    for (index, x) in enumerate(vector1):
        a = gmpy.mpz(x)
        b = gmpy.mpz(vector2[index])
        sum += a * b
    print "Case #%d: %s" % (i, sum)
