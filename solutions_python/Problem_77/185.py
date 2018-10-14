import copy
import sys
import re
import random

def randomize(list, freeze):
    toRandomize = []
    for i in range(0, len(list)):
        if i not in freeze:
            toRandomize.append(list[i])
    random.shuffle(toRandomize)
    for i in range(0, len(list)):
        if i not in freeze:
            list[i] = toRandomize.pop()

def main():
    infile = open(sys.argv[1])
    T = int(infile.readline().strip())

    for i in range(0, T):
        infile.readline()
        N = [int(o) for o in infile.readline().strip().split()]
        Nsorted = copy.copy(N)
        Nsorted.sort()
        
        numInPlace = 0
        for j in range(0, len(N)):
            if j+1 == N[j]:
                numInPlace += 1

        print "Case #" + str(i+1) + ":", str(len(N)-numInPlace) + ".000000"

if __name__ == "__main__":
    main()
