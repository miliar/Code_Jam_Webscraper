import numpy as np
import random as rx
import math
import os

def main():

    f = open('input.txt', 'r')
    numcases = int(f.readline().rstrip('\n'))

    for i in range(1,numcases+1):

        x = f.readline().rstrip('\n')
        x = int(x)

        while(1):

            if isvalid(x):
                print "Case #" + str(i)+ ":" + str(x)
                break
            else:
                x = x-1


def isvalid(x):
    x = str(x)
    for i in range(len(x)-1):
        if int(x[i]) > int(x[i+1]):
            return False
    return True

if __name__ == "__main__":
    main()