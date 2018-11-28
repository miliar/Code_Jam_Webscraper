import sys
import re

def oppose(E, D):
    f = False
    if len(E) <= 1:
        return False
    for d in D:        
        a = str(E).find(d[0])
        b = str(E).find(d[1])
        if a <> -1 and b <> -1:
            f = True
    return f

def combine(E, C):
    if len(E) > 1:
        for c in C:
            if E[0] == c[0] and E[1] == c[1]:
                return c[2]
            if E[0] == c[1] and E[1] == c[0]:
                return c[2]
    return False

for k in range(1, int(sys.stdin.readline())+1):
    line = sys.stdin.readline().rstrip().split()
    
    C = []
    D = []
    N = []
    
    c = int(line.pop(0))
    if c <> 0:
        for i in range(c):
            C.append(line.pop(0))
    
    d = int(line.pop(0))
    if d <> 0:
        for i in range(d):
            D.append(line.pop(0))
            
    n = int(line.pop(0))
    if n <> 0:
        N = line.pop(0)

    A = []
    S = []
    old = -1
    
    for cc in N:
        S.append(cc)
    
    if len(N)==1 or (int(c) == 0 and int(d) == 0):
        print "Case #%d: [%s]"%(k, ", ".join(S))
    else:
        R = []
        #print N
    
        E = [] # element list
    
        while S <> []:
            item = S.pop(0)
            # invoke item to list
            E.insert(0, item)
            #print item, E
        
            c = combine(E, C)
            if c :
                E.pop(0)
                E.pop(0)
                E.insert(0, c)
            else:
                if oppose(E, D):
                    E = []

        E.reverse()
        print "Case #%d: [%s]"%(k, ", ".join(E))
    
    
    