from math import log,ceil

def f(L,P,C):
    
    x = log(P/float(L) , C)
    
    if x>1:
        return int(ceil(log(x,2)))
    else:
        return 0


with open('b.in') as infile:
    T = int(infile.readline())
    with open('b.out','w') as outfile:
        j = 1
        while j<=T:
            L,P,C = tuple(map(int, infile.readline().split()))
            outfile.write('Case #%d: %s\n' %(j,f(L,P,C)))
            j += 1
            
        
    

