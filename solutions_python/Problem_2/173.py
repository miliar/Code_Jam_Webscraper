def ttoi(a):
    return int(a[0:2])*60+int(a[3:5])

def go():
    f=open('2.txt')
    for x in range(int(f.readline())):
        alist=[]
        blist=[]
        atrains=0
        btrains=0
        t=int(f.readline())
        lines=f.readline().split()
        alines=int(lines[0])
        blines=int(lines[1])

        for a in range(alines):
            l=f.readline().split()
            alist.append((ttoi(l[0]),'out'))
            blist.append((ttoi(l[1])+t,'in'))
            

        for b in range(blines):
            l=f.readline().split()
            blist.append((ttoi(l[0]),'out'))
            alist.append((ttoi(l[1])+t,'in'))

        alist.sort()
        blist.sort()

        
        trainshere=0
        for y in alist:
            if y[1]=='in':
                trainshere+=1
            if y[1]=='out':
                trainshere-=1
                if trainshere==-1:
                    trainshere=0
                    atrains+=1
        trainshere=0
        for y in blist:
            if y[1]=='in':
                trainshere+=1
            if y[1]=='out':
                trainshere-=1
                if trainshere==-1:
                    trainshere=0
                    btrains+=1
                
        print "Case #%d: %d %d"%(x+1,atrains,btrains)
    f.close()

go()

        

        
        
