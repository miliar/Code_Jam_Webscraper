

import sys
import math

def isPerfect(n):
    root = int(math.sqrt(n))
    if root * root == n:
        return (True, root)
    return (False, root)

def isPalin(n):
    s = "{0}".format(n)
    r = reversed(s)
    i = 0
    for j in r:
        if s[i] != j:
            return False
        i = i + 1
    return True

def PalinInRange(x, y):
    count = 0
    for i in range(x, y + 1):
        (result, root) = isPerfect(i)
        #print "i = {0}, root = {1}, i_palin = {2}, root_palin = {3}, perfect = {4}". \
               # format(i, root, isPalin(i), isPalin(root), result)
        if result and isPalin(root) and isPalin(i):
            count = count + 1
    return count

def runIt():
    input = sys.stdin
    n_tests = int(input.readline(), 10)
    
    for i in range(n_tests):
        line = input.readline().split(' ')
        (x, y) = map(int, line)
        print ("Case #{0}: {1}".format(i + 1, PalinInRange(x, y)))

runIt()
