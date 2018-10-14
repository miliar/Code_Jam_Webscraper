fin = open("C-small-attempt0.in", "r")
fout = open("C-small.out", "w")


def check(P):
    hh = {}
    for j in P:
        for i in P:
            if i == j:
                continue
            if j - i in P: 
                if j - i != i:
                    print i , j - i
                    print j       
                    fout.write("%i " %(i))
                    fout.write("%i\n" %(j-i))                
                    fout.write("%i\n" %(j))
                    return 1
            if i+j not in hh:   
                hh[i+j] = {i,j}    
            if hh[i+j] != {i,j} :
                    for k in hh[i+j]:
                        print k
                        fout.write("%i " %(k))
                    print i,j
                    fout.write("\n%i " %(i))                
                    fout.write("%i\n" %(j))                     
                    return 1 
            for k in P:
                if k != i and k != j:
                    if i+j+k not in hh:   
                        hh[i+j+k] = {i,j,k}    
                    if hh[i+j+k] != {i,j,k} :
                            for l in hh[i+j+k]:
                                print l
                                fout.write("%i " %(l))
                            print i,j,k
                            fout.write("\n%i " %(i))                
                            fout.write("%i " %(j))                     
                            fout.write("%i\n" %(k)) 
                            return 1                                 
                    
    return 0

N = int(fin.readline())
for n in range(1,N+1):
    r = "Case #" + str(n) +":"
    print r
    fout.write("Case #%i:\n" %(n))
#    P = {int(i) for i in fin.readline().split()}
    P = {}
    ind = 0
    flag = 1
    for i in fin.readline().split():
        if flag:
            flag = 0
            continue
        ind = ind + 1
        P[int(i)]= ind
    st = ""

    flag = check(P)
    if flag == 0:
        print "Impossible"
        fout.write("Impossible")        
#    print st
    
#    print r + str(sum)    
#    fout.write("\n")
    P = {}
fout.close()




