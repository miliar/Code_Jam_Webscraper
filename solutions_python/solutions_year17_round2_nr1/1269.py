fin = open('1.in')
fout = open('1.out', 'w')


T = int(fin.readline())

for iter in range(0, T):
    D,N = fin.readline().split(" ")
    D = float(D)
    N = int(N)
    
    p = []
    
    for i in range(0,N):
        k_i, s_i = fin.readline().split(" ")
        p.append((float(k_i),float(s_i)))
    
    p.sort(key=lambda x: x[0], reverse=True)
    
    m = (D-p[0][0]) / p[0][1]
    
    for i in range(1,N):
        temp = (D - p[i][0])/p[i][1]
        if temp > m:
            m = temp
        
    
    
    fout.write("Case #%d: " %(iter+1))
    
    fout.write("%.6f" %(D/m))
    fout.write('\n')
    
    
fin.close()
fout.close()