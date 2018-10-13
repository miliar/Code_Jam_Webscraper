g=open('output.txt','w')
with open('A-small-attempt3.txt','r') as f :
    t=int(f.readline())
    c=1
    while True :
        l=[]
        m=[]
        x=int(f.readline())
        for i in range(4):
            l.append(f.readline().split())
        y=int(f.readline())
        for i in range(4):
            m.append(f.readline().split())
        l=[ [int(l[i][j]) for j in range(4)] for i in range(4) ]
        m=[ [int(m[i][j]) for j in range(4)] for i in range(4) ]
        n=list(set(l[x-1]).intersection(set(m[y-1])))
        if len(n)==0 :
                g.write("Case #"+str(c)+": Volunteer cheated!\n")
        elif len(n)==1:
                g.write("Case #"+str(c)+": "+str(n[0])+"\n")
        else:
                g.write("Case #"+str(c)+": Bad magician!\n")
        
        c=c+1
        t=t-1;
        if t==0:
            break
g.close()
