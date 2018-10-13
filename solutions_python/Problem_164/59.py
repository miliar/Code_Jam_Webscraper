from itertools import combinations

# Brute force for 1 or 2 hikers
def brute2(D, M):
    if len(D) == 1:
        return 0
    elif len(D) == 2:
        if M[0] == M[1]:
            return 0
        elif M[0] < M[1]:
            MS = M[0]
            ML = M[1]            
            DS = D[0]
            DL = D[1]                    
        else:
            ML = M[0]
            MS = M[1]
            DL = D[0]
            DS = D[1]
        t1 = ML*(ML-MS)*(360-DL)
        t2 = (360+DL-DS)*ML*MS
        if t1 < t2:
            return 0
        else:
            return 1
    else:
        print "MAYDAY"
        return 0

def brute(lines):    
    D = []
    M = []
    for line in lines:
        D.extend([line[0]]*line[1])
        M.extend(range(line[2], line[2]+line[1]))
    return brute2(D, M)
    

def solve(in_name, out_name):
    fin = open(in_name, 'r');
    L = [map(int, x.strip().split()) for x in fin.readlines()]
    fin.close()    
    T = L[0][0]
    out = []
    lnr = 1
    for i in xrange(T):
        N = L[lnr][0]        
        out.append("Case #" + str(i+1) + ": " + str(brute(L[lnr+1:lnr+N+1])) + "\n")
        lnr += (N+1)
        
    fout = open(out_name, 'w')
    fout.writelines(out)
    fout.close()
    return

#sys.setrecursionlimit(1010)	
#solve('C-test.in', 'C-test.out')
solve('C-small-1-attempt0.in', 'C-small-1-attempt0.out')
