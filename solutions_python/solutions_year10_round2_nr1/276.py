from fractions import gcd
from itertools import izip


def mkcount(exists,creates):
    mkdict = {tuple():0}
    for exist in exists:
        key = []
        for tok in exist:
            key.append(tok)
            mkdict[tuple(key)] = 0
    mkcount = 0
    for create in creates:
        key = []
        for tok in create:
            key.append(tok)
            if not mkdict.has_key(tuple(key)):
                mkcount += 1
                mkdict[tuple(key)] = 0
    return mkcount

def print_res(caseno,res):
    print "Case #%d: %s" %(caseno,res) 

def main():
    for case in xrange(1,int(raw_input())+1):
        N,M = [long(w) for w in raw_input().split(' ')]
        exists = []
        for i in range(N):
            line = [w for w in raw_input().split('/') if w]
            exists.append(line)
        creates = []
        for i in range(M):
            line = [w for w in raw_input().split('/') if w]
            creates.append(line)
        print_res(case,mkcount(exists,creates))

if __name__=="__main__":
    main()
