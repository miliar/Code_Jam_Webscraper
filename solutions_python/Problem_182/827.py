import sys, string
import time
import numpy as np
from copy import copy, deepcopy

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

def check_order(M,N):
    for i in range(N):
        if list(sorted(M[i,:])) != list(M[i,:]):
            return False
        if list(sorted(M[:,i])) != list(M[:,i]):
            return False
    return True

def find_missing(M,N,P):
    L = []
    for i in range(N):
        L.append(list(M[i,:].flatten()))
        L.append(list(M[:,i].flatten()))
    for i in range(len(L)):
        L[i] = [int(x) for x in L[i]]
    #~ print L
    #~ print P
    for l in L:
        try: P.remove(l)
        except: return l
        #~ print P


def place_v(M,N,i,p):
    for k in range(N):
        if M[k,i] and M[k,i] != p[k]:
            #~ print M,i,p, "vnok"
            return False
    #~ print M,i,p,'vok'
    M[:,i] = p
    return True

def place_h(M,N,i,p):
    for k in range(N):
        if M[i,k] and M[i,k] != p[k]:
            #~ print M,i,p, "hnok"
            return False
    #~ print M,i,p,'hok'
    M[i,:] = p
    return True

def try_fill(N, H, P, hd):
    M = np.zeros([N,N])
    
    # these are clear
    M[0][0] = H[0]
    M[N-1][N-1] = H[-1]
    #~ print M
    
    #~ print H.count(H[0])
    #~ print H.count(H[N-1])
    if H.count(H[0]) == 1:
        rangeN = reversed(range(N))
    else:
        rangeN = range(N)
    
    placed = [False] * len(P)
    for i in rangeN:
        # try to place list p on line/column i

        #~ Px = enumerate(P) if hd & (1 << i) else reversed(list(enumerate(P)))
        #~ M0 = deepcopy(M)
        #~ p0 = deepcopy(placed)
        
        vplaced = False
        hplaced = False
        for k,p in enumerate(P):
            if placed[k]:
                continue
            if hd & (1 << i):
                # first vertical, second horizontal
                if not vplaced:
                    if place_v(M,N,i,p): placed[k] = 'V'; vplaced = True
                else:
                    if place_h(M,N,i,p): placed[k] = 'H'; hplaced = True
            else:
                # first vertical, second horizontal
                if not hplaced:
                    if place_h(M,N,i,p): placed[k] = 'H'; hplaced = True
                else:
                    if place_v(M,N,i,p): placed[k] = 'V'; vplaced = True
        
        #~ if i == N-1:
            #~ print M
            #~ raise SystemExit
        
        if 0:
         if not hplaced:
          for k,p in enumerate(P):
            M = M0
            placed = p0
            # the other way?
            if not hplaced:
                if place_h(M,N,i,p): placed[k] = 'H'; hplaced = True
            else:
                if place_v(M,N,i,p): placed[k] = 'V'; vplaced = True
            

    #~ print placed
    #~ print M
    #~ print P

    if False in placed:
        return None
    if check_order(M,N):
        return M

T = readint()
for t in range(T):
    N = readint()
    P = []
    H = []
    for i in range(2*N-1):
        P.append(readlist())
        H = H + P[-1]
    H = sorted(list(H))
    
    #~ if t != 31: continue
    
    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),
    
    #~ print P
    for hd in range(1 << N):
        M = try_fill(N, H, P, hd)
        if M is not None:
            #~ print M
            sol = find_missing(M,N,P)
            #~ print sol
            sol = [str(s) for s in sol]
            print " ".join(sol)
            break
    
