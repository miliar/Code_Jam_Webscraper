#codejam 4/17/15
import math as m
import time
#import codejam
import sys
sys.setrecursionlimit(100)#1100) #we need 1000 max

#filename = r'c:\g\1A\1-test.in.txt'
filename = r'c:\g\1A\A-large.in'
#filename = r'c:\g\A1\1-large.in'
foutname = r'c:\g\1A\1-out-large.txt'
#foutname = r'c:\g\1A\1-out-large.txt'

FILE = open(filename)
FOUT = open(foutname,"w")
T = int(FILE.readline())

def ceildiv(x, d):#like x//d but ceiling, for positives only
    return (x + (d-1)) // d

def sol1(M, dbg): #first method, given samples in array M, which is of length 2 to 1000
    S = M[0] #number at start
    E = 0 #total eaten
    pmj = M[0] #previous mj
    for mj in M[1:]:
        D = mj - pmj #delta
        if D>0: #more were put on plate, none eaten
            pass
        elif D<0: #some were removed, must have been eaten
            if dbg: print "D<0: D=",D,", ate",-D," so total eaten=",(E-D)
            E -= D
        else: #no change
            pass
        pmj = mj
    return E

def sol2(M, dbg): #second method, eats at constant rate
    #first find minimum eating rate - largest decline
    changes = [b-a for a,b in zip(M[:-1],M[1:])]
    R = abs(min(changes))
    E = 0 #number eaten
    if dbg: print "sol2 R=",R #minimum eating rate
    P = M[0] #number on plate at start
    pmj = M[0] #previous mj
    for mj in M[1:]:
        P2 = max(0,P - R) #she would eat down to this if none were added
        #if dbg: print "See mj=",mj,"so ate",(P-P2)," P2=",P2
        E += (P - P2)
        #if mj > P2: #more were added, assumed an instant before time sample (for minimum)
        #    pass
        #else: #some (or none) were removed
        #    pass #must have been eaten
        P = mj
        pmj = mj
    return E

dbg=0
if dbg: print ""
if 1:
  t0 = time.time()
  sumz = 0
  for i in range(1,T+1):
    rawline = FILE.readline().split(' ')
    D = int(rawline[0]) #number of samples at 10 second intervals
    if len(rawline)>1: #trick to check known answers
        manual_ans = [int(a) for a in rawline[-2:]]
    else:
        manual_ans = None

    s = FILE.readline()
    if s[-1]<'0': s=s[:-1]#strip newline
    P = [int(ps) for ps in s.split(' ')]
    if dbg: print "Case #" + str(i)+": D=",D," ["+(' '.join([str(xp) for xp in P]))+']',("manual_ans="+str(manual_ans) if manual_ans else "")
    #if dbg and manual_ans: print "manual_ans = ",manual_ans

    z1 = sol1(P, 0)
    z2 = sol2(P, dbg)
    if dbg: print "  ==> ",z1,z2
    sumz += z1
    msg = 'Case #' + str(i) + ': ' + str(z1)+' '+str(z2)
    if dbg:
        if manual_ans: print msg+ (" 1 is OK!" if manual_ans[0]==z1 else "1 DIFF!") + (" 2 is OK!" if manual_ans[1]==z2 else "2 DIFF!")
        else: print msg
    if not dbg and i%10==1: print msg
    FOUT.write(msg + "\n")
    if manual_ans!=None:
        if manual_ans[0]!=z1 or manual_ans[1]!=z2: print "...DIFFERENT! ",manual_ans," but we got: ",(z1,z2)
    if dbg: print ""
  print "finished",T,"cases,", round(time.time() - t0,3),"s, sumz:",sumz
FOUT.close()
FILE.close()
