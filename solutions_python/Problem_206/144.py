import sys

def solve(D, horses):
    time = max((float)(D - K) / S for K, S in horses)
    return D / time

with open(sys.argv[1]) as infile:
    cases = int(infile.readline())
    for i in range(cases):
        D, N = [int(x) for x in infile.readline().split()]
        horses = []
        for j in range(N):
            horses.append(tuple([int(x) for x in infile.readline().split()]))
        print "case #%d:" % (i+1), solve(D, horses)