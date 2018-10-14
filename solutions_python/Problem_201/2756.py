from sys import stdin
import numpy as np

def pos(n):
    l = (n-1)/2
    r = n-1-l
    return [l,r]

num_cases = int(stdin.readline())
for case_index in xrange(1, num_cases+1):
    n,k = map(int,stdin.readline().strip().split(' '))

    free = np.array([n])
    res = []

    for i in range(k):
        i = np.argmax(free)
        val = free[i]
        res = pos(val)

        free = np.delete(free,i)
        free = np.insert(free,i,res)


    print "Case #" + str(case_index) + ": " + " ".join(map(str,res[::-1]))
