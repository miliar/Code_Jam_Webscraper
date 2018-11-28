fin= open('short.txt','r')
lt = int(fin.readline())
s=0

for line in range(lt):
        s=s+1
        pt=fin.readline()
        splt=pt.split()
        g = int(splt[0])
        l=[]
        c=0
        for x in range(0,g):
                n=[]
                point=fin.readline()
                slit=point.split()
                n.append(int(slit[0]))
                n.append(int(slit[1]))
                l.append(n)
        for x in range(0,g-1):
                for y in range(x+1,g):
                        if ((l[x][0]<l[y][0]) and (l[x][1]>l[y][1])) or ((l[x][0]>l[y][0]) and (l[x][1]<l[y][1])):
                                c=c+1
        print 'Case #%d: %d' %(s,c)        
                
