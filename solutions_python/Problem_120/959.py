import sys
from math import floor
from mpmath import sqrt

def calc(r,t):
    return floor(1 +(.25* (-3-(2*r)+sqrt(1-(4* r)+(4 *(r**2))+(8* t)))))
    #return floor(1 + .25*(-3-2*r+sqrt(1-4*r+4*r*r+8*t)))
        

if __name__=="__main__":
    filename = sys.argv[1]
    f = open(filename, 'r')
    numtests = int(f.readline())
    for i in range(1, numtests+1):
        l = f.readline().split()
        print("Case #" + str(i) + ": " + str(int(calc(int(l[0]), int(l[1])))))
