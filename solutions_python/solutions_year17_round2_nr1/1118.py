matrix = None
NXmask = None
NPmask = None

def maxspeed(D,Kls,Sls):

    tmax = -1

    for i in range(len(Kls)):
        t = (D-Kls[i])/Sls[i]
        if t > tmax:
            tmax = t
    return D/tmax

import sys

def main():

    with open(sys.argv[1]) as f:
        m = int(f.readline())
        for i in range(m):
            D,N = f.readline().strip().split()
            D,N = int(D),int(N)
            Kls,Sls = [], []
            for j in range(N):
                K,S = f.readline().strip().split()
                Kls.append(float(K))
                Sls.append(float(S))
            s = maxspeed(D,Kls,Sls)
            print("Case #{:d}: ".format(i+1)+str(s))
main()
