#!/usr/bin/env python3

from bisect import *

def normal_war(naomi ,ken, rounds):
    npoints=0
    kpoints=0
    while rounds>0:
        nchoice=naomi.pop()
        kindex = bisect_right(ken, nchoice)
        if kindex==rounds:
            kindex=0
        kchoice=ken.pop(kindex)
        if kchoice>nchoice:
            kpoints+=1
        else:
            npoints+=1
        rounds-=1
    return npoints

def deceitful_war(naomi, ken, rounds):
    npoints=0
    kpoints=0
    while rounds>0:
        naomi_highest=naomi[-1]
        if naomi_highest>ken[-1]:
            naomi.pop(rounds-1)
            ken.pop(rounds-1)
            npoints+=1
        else:
            naomi.pop(0)
            ken.pop(rounds-1)
            kpoints+=1
        rounds-=1
    return npoints

def get_points(naomi, ken, rounds=None):
    if not rounds:
        rounds=len(naomi)
    naomi.sort()
    ken.sort()
    naomi2=naomi.copy()
    ken2=ken.copy()
    return (deceitful_war(naomi,ken,rounds),normal_war(naomi2, ken2, rounds))
    return npoints

def parse_file(filename):
    fo=open(filename)
    cases=[]
    test_cases=int(next(fo).strip())
    for j in range(test_cases):
        rounds=int(next(fo).strip())
        naomi=[float(i) for i in next(fo).strip().split()]
        ken=[float(i) for i in next(fo).strip().split()]
        cases.append((naomi,ken,rounds))
    return cases

def main(filename):
    cases=parse_file(filename)
    for index,case in enumerate(cases):
        out=get_points(*case)
        print("Case #{0}: {1} {2}".format(index+1, out[0], out[1]))

if __name__=="__main__":
    from sys import argv
    main(argv[-1])
