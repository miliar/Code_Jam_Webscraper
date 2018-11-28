#!/usr/bin/env python
# google code jam 2011
# round 1a, problem a
# Joseph Lee <GengarKhan@gmail.com>
# 5/20/11

import sys

def main(name_in, name_out):
    infile = open(name_in, 'r').read().strip().split('\n')[1:]  # input 1st arg
    if name_out != None:
        outfile = open(name_out, 'w')    # output file, 2nd cmd-line arg
    else:
        outfile=sys.stdout
    casenum=1
    for i in infile:
        outfile.write('Case #%d: %s\n' %(casenum, test_case(i)))
        casenum=casenum+1
    if outfile != sys.stdout:
        outfile.close()
    return 0


# main test case calculation method
def test_case(test_in):
    N, Pd, Pg = parse_input(test_in)
    #if Pg == 100 and Pd != 100: # Pg can't be 100 if Pd isn't 100
    #    return 'Broken'
    if Pg == 100:
        if Pd == 100:
            return 'Possible'
        else:
            return 'Broken'
    elif Pg == 0:
        if Pd == 0:
            return 'Possible'
        else:
            return 'Broken'
    Dlist=CheckPd(N, Pd)
    #print('%d %d %d: %s'%(N, Pd, Pg, str(Dlist)))
    if len(Dlist) > 0:
        #if CheckPg(Dlist, Pd, Pg) == True:
        #    return 'Possible'
        return 'Possible'
    return 'Broken'


# parse input from command line
def parse_input(test_in):
    ln = test_in.strip().split()
    return int(ln[0]), int(ln[1]), int(ln[2])


def CheckPd(N, Pd):
    possD=[]    # possible D-vals
    for D in range(1, N+1):
        for Wd in range(0, D+1):
            if int((float(Wd)/D)*100)==Pd:
                if (float(Wd)*100)/D-float(Pd) < 0.001:
                    possD.append(D)
    return possD


# returns True or False if possible
def CheckPg(Dlist, Pd, Pg):
    for D in Dlist:
        Wd=(D*Pd)/100  # wins today
        Gdiff=100-D
        if (Wd+Gdiff) >= Pg:
            if Wd <= Pg:
                return True
    return False

if __name__=='__main__':
    name_in=sys.argv[1]
    if len(sys.argv) >= 3:
        name_out=sys.argv[2]
    else:
        name_out=None
    main(name_in, name_out)

