#!/usr/bin/python


import fractions
import sys


input_file = open('B-small-attempt1.in')
output_file = open('B-small-attempt1.out', 'w')

C = int(input_file.readline())



def gcd(tt):
    w = 2
    acc_gcd = fractions.gcd(tt[0], tt[1])
    while w < len(tt):
        acc_gcd = fractions.gcd(acc_gcd, tt[w])
        w += 1
    return acc_gcd


#    if len(tt) <= 2:
#        return fractions.gcd(tt[0], tt[1])
#
#    return fractions.gcd(gcd(tt[0:-1]), tt[-1])


for c in range(C):
    t = map(int, input_file.readline().split(' '))
    del t[0]

    diffs = []
    i = 0
    while i < len(t):
        u = i + 1
        while u < len(t):
            if t[i] - t[u] != 0:
                diffs.append(abs(t[i] - t[u]))
            u += 1
        i += 1
    limit = min(diffs)
#    limit = max(t)

    max_gcd = 1
    result = 0
    i = 0
    while i <= limit:
#        print i
        tt = map(lambda x: x + i, t)
        u = 0
        new_gcd = gcd(tt)
        if new_gcd > max_gcd:
            max_gcd = new_gcd
            result = i
        i += max_gcd

    output_file.write("Case #" + str(c + 1) + ": " + str(result) + "\n")
    sys.stdout.write("Case #" + str(c + 1) + ": " + str(result) + " " + str(max_gcd) + "\n")


input_file.close()
output_file.close()
