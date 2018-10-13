fin = open("A.in",'r')
fout = open("A.out",'w')

tmp = fin.readline()
T = eval(tmp)
for t in range(T):
    tmp = fin.readline().split()
    N = eval(tmp[0])
    S = [0] * N
    for i in range(N):
        S[i] = eval(tmp[i + 1])
    M = [0] * N
    flag  = [0]* N
    total = sum(S)
    n = N
    k = 1
    kf = 0
    ks = 0
    while k != kf:
        k = kf
        kn = n
        for i in range(N):
            if flag[i] == 0:               
                M[i] = ((2.0 * total - ks)/ kn - S[i]) / total * 100
                if M[i] <= 0:
                    M[i] = 0
                    n -= 1                        
                    flag[i] = 1
                    ks += S[i]                
        kf = sum(flag)
    print >> fout,"Case #%d:" %(t+1),
    for i in range(N-1):
        print >> fout,"%.6lf" %M[i],
    print >> fout,"%.6lf" %M[N-1]
   
fin.close()
fout.close()