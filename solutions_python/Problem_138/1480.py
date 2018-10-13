import sys
sys.setrecursionlimit(10000)
import pdb

def deceitful_war(naomi, ken):
    if naomi[0]<ken[0]:
        if(len(naomi)>1):
            return deceitful_war(naomi[1:], ken[:-1])
        else:
            return 0
    else:
        if(len(naomi)>1):
            return 1 + deceitful_war(naomi[1:], ken[1:])
        else:
            return 1

def war(naomi, ken):
    if naomi[-1]>ken[-1]:
        if(len(naomi)>1):
            return 1 + war(naomi[:-1], ken[1:])
        else:
            return 1
    else:
        if(len(naomi)>1):
            return war(naomi[:-1], ken[:-1])
        else:
            return 0

fh = open(sys.argv[1])
T = int(fh.readline().rstrip())
for i in range(T):
    fh.readline()
    naomi = map(float, fh.readline().rstrip().split(" "))
    ken = map(float, fh.readline().rstrip().split(" "))
    naomi = sorted(naomi)
    ken = sorted(ken)
    print "Case #{0}: {1} {2}".format(i+1, deceitful_war(naomi, ken),
                                      war(naomi, ken))
