from math import sqrt, pow, log, ceil, log10
from sys import stdin, setrecursionlimit

setrecursionlimit(100000)
debug = 0

def solve(N, array):

    rep = 0
    howmany = 0
    i = 0

    for c in array:

        if debug:
            print "curr (i, howmany, rep, c): ", i, howmany, rep, c

        if int(c) > 0:

            if howmany >= i:
                howmany += int(c)
            else:
                rep += i - howmany
                howmany += rep + int(c)
        
        if debug:
            print "afte (i, howmany, rep, c): ", i, howmany, rep, c
            print

        i += 1

    return rep

T = int(stdin.readline())

for i in range(1,T+1):
    
    N, array = stdin.readline().split(' ')
    N = int(N)
    array = array.rstrip()

    print "Case #" + str(i) + ":", 

    if debug:
        print N, " then ", array

    # if len(array) != N + 1:
    #     print "Error"
    #     exit(-1)

    print solve(N, array)
