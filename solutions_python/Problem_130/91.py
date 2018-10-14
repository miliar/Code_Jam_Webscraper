#!/usr/bin/python
import sys

f_input = open(sys.argv[1])
linenums = int(f_input.readline().rstrip())

def solve(T, P):
    if 1<<T == P:
        return P-1, P-1
    ## worstcase
    # 0 = always 0
    # 1 = N/2  .. 
    # 2 = N/2
    # 3 = N/4
    # 4 = N/4
    prisebit = 0
    lestP = str(bin(P-1))[2:]
    if(len(lestP) < T): prisebit = 0
    else:
        while(lestP[prisebit]=="1"):
    
            if(len(lestP)-1==prisebit):
                print "here", T, P
                break
            prisebit+=1
    worstcase = (1<<(prisebit+1))-2
    
    ## bestcase
    # N .. N L....L
    # N-1 .. N/2 WL....
    # N-2 .. N/2 WL...
    # N-3 .. N/4 WL...W
    # N-4 .. N/4 WL...W
    # N-5 .. N/4 
    # N-6 .. N/4+N/8
    prisebit = 0
    lestP = str(bin(P))[2:]

    if T == len(lestP)-1:
        print "here", T, P
        bestcase = (2<<T-1)
    else:
        bestcase = (2<<T-1) - (2<<(T-len(lestP))) 

    
    return worstcase, bestcase
    
for i in xrange( linenums ):
    T, P = map(int, f_input.readline().rstrip().split(" ") )
    worst, best = solve(T, P)
    sys.stdout.write("Case #"+str(i+1)+": "+str(worst)+" "+str(best)+"\n")
