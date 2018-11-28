from sys import argv
import math

#f = open(sys.argv[1])
f = open("B-large.in")
cases = int(f.readline())


def checkLawnmower(array, N, M):
    transposed_array = zip(*array)
    for k in range(N):
        for l in range(M):
            target = array[k][l]
            if target < max(array[k]) and\
            target < max(transposed_array[l]):
                return False
    return True
    

for i in range(cases):
    count = 0
    N,M = map(int, f.readline().split())
    array = []

    for j in range(N):
        array.append(map(int, f.readline().split()))
    
    if checkLawnmower(array, N, M):
        print "Case #%d: YES" % (i + 1)
    else:
        print "Case #%d: NO" % (i + 1)

f.close()
