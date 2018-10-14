#!/usr/bin/python

from sys import stdin

def istidy(num_l):
    for n in range(len(num_l)-1):
        if (num_l[n+1] < num_l[n]):
            return (False, n)
    return (True, 0)


def maxtidy(num):
    num_l = [int(d) for d in str(num)]
    tidy, n = istidy(num_l)
    while not tidy:
        num_l[n] = num_l[n] - 1
        for r in range(n+1, len(num_l)):
            num_l[r] = 9
        tidy, n = istidy(num_l)
    return int(''.join([str(d) for d in num_l]))

nb_tc = int(stdin.readline())
for i in range(nb_tc):
    num = int(stdin.readline())
    print "Case #" + str(i+1) + ": " + str(maxtidy(num))

