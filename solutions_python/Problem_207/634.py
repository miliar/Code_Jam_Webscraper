import numpy as np
import sys

def readData():
    line = sys.stdin.readline().split()
    N, R, O, Y, G, B, V = map(int, line)
    
    return N, R, O, Y, G, B, V 


#R + Y = O
#Y + B = G
#R + B = V

def solve(N, R, O, Y, G, B, V ):
    #print N, R, O, Y, G, B, V 
    if ((V > Y) or ((V == Y and V > 0) and (R+O+G+B) > 0)) or ((G > R) or ((G == R and G > 0) and (O + Y + B + V) > 0)) or ((O > B) or ((O == B and O > 0) and (R + Y + G + V > 0))):
        return "IMPOSSIBLE"
    
    #if G > 0:
        #R -= G + 1
    #if V > 0:
        #Y -= V + 1
    #if O > 0:
        #B -= O + 1
        
    #print "G, V, O:", G, V, O
    
    letter = {0: 'R', 1: 'Y', 2: 'B'}
    RYB = np.array([R,Y,B], dtype=int)
    ixorder = np.argsort(RYB)
    i = 0
    start = ixorder[2]
    last = -1
    
    
    sol = np.chararray(N)
    
    if G > 0:
        start = 0
        if R > G:
            #print "ok"
            sol[i] = "R"
            i += 1
            RYB[0] -= 1
        for j in xrange(G):
            #sys.stdout.write("GR")
            sol[i] = "G"
            sol[i+1] = "R"
            i += 2
            #print i+1*j, i+2*j+2
            #print "sol:", sol
            #print "G:", G
        RYB[0] -= G
        #i += 2*G
        #G = 0
        last = 0
        #print "i:", i
        
    if V > 0:
        if i == 0:
            start = 1
            
        if Y > V:
            sol[i] = "Y"
            i += 1
            RYB[1] -= 1
        for j in xrange(V):
            #sys.stdout.write("VY")
            sol[i] = "V"
            sol[i+1] = "Y"
            i += 2
        RYB[1] -= V
        #i += 2*V
        #V = 0
        last = 1
        
        
    if O > 0:
        if i == 0:
            start = 2
            
        if B > O:
            sol[i] = "B"
            i += 1
            RYB[2] -= 1
        for j in xrange(O):
            #sys.stdout.write("OB")
            sol[i] = "O"
            sol[i+1] = "B"
            i += 2
            #sol[i+2*j:i+2*j+2] = "OB"
        RYB[2] -= O
        #i += 2*O
        #O = 0
        last = 2
        
    #print sol
    
    
    #print "i:", i
    #print "0RYB:", RYB
    while i < N-2:
        ix = ixorder[2]
        if ix == last:
            ix = ixorder[1]
        #sys.stdout.write(letter[ix])
        sol[i] = letter[ix]
        RYB[ix] -= 1
        #print "1RYB:", RYB
        
        last = ix
        i += 1
        
        ixorder = np.argsort(RYB)
        
    #print "RYB:", RYB
            
    if i < N-1:
        if RYB[start] > 0:
            if start == last:
                return "IMPOSSIBLE"
            #sys.stdout.write(letter[start])
            sol[N-2] = letter[start]
            RYB[start] -= 1
            last = start
        else:
            ix = ixorder[2]
            if last == ix:
                ix = ixorder[1]
            #sys.stdout.write(letter[ix])
            sol[N-2] = letter[ix]
            RYB[ix] -= 1
            last = ix
        i += 1
    
    if i < N:
        ixorder = np.argsort(RYB)
        ix = ixorder[2]
        if ix == last:
            return "IMPOSSIBLE"
        #sys.stdout.write(letter[ix])
        sol[N-1] = letter[ix]
          
    #sys.stdout.write("\n")
    
    return ''.join(sol)
        
    
    
    
    



if __name__ == "__main__":
    T = int(sys.stdin.readline())
    result = 0
    for t in xrange(T):
        data = readData()
        result = solve(*data)
        print "Case #"+str(t+1)+":", result
        #result
        
