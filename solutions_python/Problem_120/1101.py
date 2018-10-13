import os, math, sys
from pprint import pprint
import copy

def readints(fp):
    return map(int, fp.readline().split())


def solve():
    pass


# def area(r):
#     return math.pi*r*r
#
# def paint_used(r):
#     return area(r+1) - area(r)


def paint_used(r):
    return 2*r*r + r

# def num_rings(ml,r):
#     return int((math.sqrt(8*ml + r*r) - r)/4)

def num_rings(ml,r):
    return int((math.sqrt(8*ml + 4*r*r - 4*r + 1) - 2*r + 1)/4)

# def num_rings(ml,r):
#     return int((math.sqrt(2*ml + r*r) - r)/2)

def main():

    inpath = 'A-small-attempt0.in'
    outpath = os.path.splitext(inpath)[0] + '.out'

    with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
        T = int(infile.readline())
        for t in xrange(T):
            radius, mL = readints(infile)



            rings = num_rings(mL, radius)

            outfile.write('Case #%d: %s\n' % (t + 1, rings))







if __name__ == '__main__':
    main()
