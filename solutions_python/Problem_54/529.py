#!/usr/bin/env python2.6

import math
import fractions

def main(fin,fout):
    iter = int(fin.readline())
    for i in range(iter):
        years = map(int,fin.readline().split(" ",1)[1].split(" "))
        years = sorted(years)
        diff = [0 for row in range(len(years)-1)]
        for yi in range(len(diff)):
            diff[yi] = years[yi+1]-years[yi]
        #diff = sorted[diff]
        gc = gcd(diff)
        div = years[0]/gc
        if(years[0]>div*gc):
            div += 1
        ans = div*gc - years[0]
        fout.write("Case #%d: %d\n" % (i+1,ans))

def gcd(l):
    gc = l[0]
    for i in range(len(l)-1):
        gc = fractions.gcd(gc,l[i+1])
    return gc
        

if __name__ == "__main__":
    with open("B-large.in","r") as fin:
        with open("bl.out","w") as fout:
            main(fin,fout)
    print "done"
