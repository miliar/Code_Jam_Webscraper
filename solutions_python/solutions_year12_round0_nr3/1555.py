fin = open("C-small-attempt0.in", "r")
fout = open("C.out", "w")


def reflect(nn,mm):
    n = str(nn)
    m = str(mm)
    
    ln = len(n)    
    for i in range(0,ln):
        new = n[i:ln] + n[0:i]
        if new == m :
            return True

    return False


N = int(fin.readline())
for n in range(1,N+1):
    fout.write("Case #%i: " %(n))
    P = [int(i) for i in fin.readline().split()]
    
    A = P[0]
    B = P[1]
    count = 0
    for n in range(A,B):
       for m in range(n+1,B+1 ):         
            if reflect(n,m):
                count = count + 1
    fout.write("%i" % (count) )
    fout.write("\n")                        
fout.close()
