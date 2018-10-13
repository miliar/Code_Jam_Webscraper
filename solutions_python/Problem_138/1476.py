#!/usr/bin/python

import sys

def solve_deceit(num, n=[], k=[], outf=None):
    np = 0
    ki = 0
    ni = 0

    while (ni < num):
        kc = k[ki]
        while (n[ni] <= kc):
            ni += 1
            if (ni >= num):
                return(np)
        ni += 1
        ki += 1
        np += 1

    return(np)
    
def solve_war(num, n=[], k=[], outf=None):
    kp = 0
    ki = 0
    ni = 0

    while (ki < num):
        nc = n[ni]
        while (k[ki] <= nc):
            ki += 1
            if (ki >= num):
                return(num - kp)
        ki += 1
        ni += 1
        kp += 1

    return(num - kp)

            
def run():
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    inf = open(infilename, 'r')
    outf = open(outfilename, 'w')

    cases_num = int(inf.readline())

    for i in range(cases_num):
        num = int(inf.readline())

        n = inf.readline().split()
        k = inf.readline().split()
        n = [float(elem) for elem in n]
        k = [float(elem) for elem in k]
        n.sort()
        k.sort()
        
        sd = solve_deceit(num, n, k, outf)
        sw = solve_war(num, n, k, outf)

        outf.write("Case #{0}: {1} {2}".format(int(i+1), sd, sw))
        outf.write("\n")

    inf.close()
    outf.close()

if __name__ == "__main__":
    run()
