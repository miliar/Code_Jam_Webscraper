import numpy as np
import random as rx
import math
import os

def main():

    f = open('input.txt', 'r')
    numcases = int(f.readline().rstrip('\n'))

    for qqq in range(1,numcases+1):

        x = f.readline().rstrip('\n')
        x = x.split()

        stalls = int(x[0])
        ppl = int(x[1])

        occ = np.zeros(stalls)

        for i in range(ppl):
            minv = -1
            maxv = -1
            lll = -1
            for j in range(stalls):


                if (occ[j] == 0):
                    Ls = getLs(j,occ,stalls)-1
                    Rs = getRs(j,occ,stalls)-1

                    if Ls >= Rs:
                        tempmax = Ls
                        tempmin = Rs
                    else:
                        tempmax = Rs
                        tempmin = Ls

                    if tempmin > minv:
                        minv = tempmin
                        maxv = tempmax
                        lll = j
                    elif tempmin == minv and tempmax > maxv:
                        minv = tempmin
                        maxv = tempmax
                        lll = j
            occ[lll] = 1
        print "Case #" + str(qqq) +": "+str(maxv) + " " + str(minv)

def getLs(i,occ,stalls):
    iter = i
    while (iter >= 0):
        if occ[iter]:
            return (i-iter)
        iter = iter - 1
    return (i-iter)

def getRs(i,occ,stalls):
    iter = i
    while (iter < stalls):
        if occ[iter]:
            return (iter-i)
        iter = iter + 1
    return (iter-i)

if __name__ == "__main__":
    main()