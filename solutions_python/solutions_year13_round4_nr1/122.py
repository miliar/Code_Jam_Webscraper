#!/Library/Frameworks/Python.framework/Versions/3.3/bin/python3.3
# Codejam ID 2442487
# Run with parameter
# -p for preprocessing
# -s for small input
# -l for large input
# -m=<int> for multithreading


from GCJ import GCJ

def parse(infile):
    #print(GCJ.readints(infile))
    N, M = GCJ.readints(infile)
    passengers = [GCJ.readintarray(infile) for i in range(M)]
    #matrix = [[ch for ch in GCJ.readstr(infile)] for i in range(R)]
    #matrix = [GCJ.readintarray(infile) for i in range(R)]
    #GCJ.readint(infile)
    #GCJ.readintarray(infile)
    #GCJ.readstr(infile)
    #GCJ.readstrs(infile)
    return N,M,passengers
    
def solve(data):
    N,M,passenger = data
    
    change = [0] * (N+1)
    honest = 0
    for o,e,p in passenger:
        d = e-o
        honest += p* ( (N)*(N+1) - ((N-d)*(N-d+1)))//2
        change[o] += p
        change[e] -= p
    
    payed = 0
    tickets = [0] * (N+1)
    for i in range(N+1):
        print(i, change[i])
        
        if change[i] < 0:
            dt = -change[i]
            
            step = N
            pay = N
            kk = i-1  
            while dt > 0:
                if tickets[kk] >= dt:
                    payed += pay * dt                    
                    tickets[kk] -= dt
                    dt = 0
                else:
                    payed += pay * tickets[kk]
                    dt -= tickets[kk]
                    tickets[kk] = 0
                    step -= 1
                    pay += step
                kk -= 1
                
        elif change[i] >= 0:
            tickets[i] += change[i]
            
    print(payed)
    
    return honest - payed


#if __name__ == "__main__":
GCJ('A', solve, parse, None).run()
