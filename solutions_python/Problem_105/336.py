fin = open("A.in",'r')
fout = open("A.out",'w')

def chain(m,i):
    ts = []
    for tmp in m[i]:
        ts.append(tmp)
    if len(ts) != 0:
        for k in ts:
            ts = ts + chain(m,k)
    return ts

tmp = fin.readline()
T = eval(tmp)
for t in range(T):
    print >> fout, "Case #%d:" %(t+1),
    tmp = fin.readline()
    N = eval(tmp)    
    m = [[]] 
    for i in range(N):
        m.append([])
    for i in range(N):
        tmp = fin.readline().split()
        n = eval(tmp[0])
        for j in range(n):
            m[i+1].append(eval(tmp[j+1]))
    find = 0
    for i in range(1,N+1):
        ts = chain(m,i)
        if len(list(set(ts))) < len(ts):
            print >> fout, "Yes"
            find = 1            
            break
    if find == 0:
        print >> fout, "No"
        

    
fin.close()
fout.close()