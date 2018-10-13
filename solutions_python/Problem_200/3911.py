from sys import stdin
import numpy as np

num_cases = int(stdin.readline())
for case_index in xrange(1, num_cases+1):
    n = int(stdin.readline().strip())

    tidy = map(int, str(n))
    i = len(tidy) - 2

    done = False
    while i>=0:
        if tidy[i] > tidy[i+1]:
            tidy[i] -= 1
            for j in xrange(i+1, len(tidy)):
                tidy[j] = 9
        i -= 1


    print "Case #" + str(case_index) + ": " + str(int("".join(map(str,tidy))))
