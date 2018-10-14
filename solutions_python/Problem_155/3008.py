with open('A-large.in','r') as f:
    T = int(f.readline())
    i = 1
    g = open('output.txt','w')
    for i in range(T):
        n,l=f.readline().split()
        c = 0
        s = 0
        for j in range(int(n)+1):
            if l[j] != '0':
                if j > s:
                    c = c+j-s
                    s = j
                s = s+int(l[j])
        g.write('Case #'+str(i+1)+': '+str(c)+'\n')   
        i = i+1
    g.close()
