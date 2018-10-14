#-------------------------------------------------------------------------------
# Name:        Cruise Control
# Purpose:
#
# Author:      poorb
#
# Created:     23/04/2017
# Copyright:   (c) poorb 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

def resolve(D,N,Horses):
    maxtime = -1
    for horse in Horses:
        time = (D - horse[0])/horse[1]
        maxtime = max(maxtime, time)
    return D/maxtime
def test(D,N,Horses):
    ret = resolve(D,N,Horses)
    print("D={0} N={1} Horses={2}  result={3:.6f}".format(D,N,Horses, ret))
def main():
    if True:
        answers = []
        with open("A-large.in","r") as infile:
            T = int(infile.readline())
            for i in range(T):
                D,N = map(int,infile.readline().split())
                Horses = []
                for j in range(N):
                    K,S = map(int,infile.readline().split())
                    Horses.append( (K,S))
                ret = resolve(D,N,Horses)
                answers.append(ret)
        with open("CruiseControl_out.txt","w") as outfile:
            for idx, ans in enumerate(answers):
                outfile.write("Case #{0}: {1:.6f}\n".format(idx+1, ans))

    else:
        test(2525,1,[(2400,5)])
        test(300,2,[(120,60),(60,90)])
        test(100,2,[(80,100),(70,10)])
if __name__ == '__main__':
    main()
