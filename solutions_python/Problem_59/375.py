import sys, string

def countMD(exDirs, nDirs):
    mks=0
    for dr in nDirs:
        drLst=dr.split("/")
        minMks=len(drLst)-1
        
        for ex in exDirs:
            actualMks=len(drLst)-1
            exLst=ex.split("/")
            for i,d in enumerate(drLst):
                
                if i==0 or i>= len(exLst):
                    continue
                if d==exLst[i]:
                    actualMks-=1
                else:
                    break
            
            if actualMks<minMks:
                minMks=actualMks
        print  minMks,  dr
        mks+=minMks
        exDirs.append(dr)
                
    return mks
    

def runRC():
    print sys.argv
    fin=open(sys.argv[1],'r')
    fout=open("res.out", "w")
    t=int(fin.readline())
    p=1
    while(p<=t):
        nm=fin.readline().split(" ")
        n=int(nm[0])
        m=int(nm[1])
        exDirs=[]
        newDirs=[]
        ed=0
        nd=0
        while ed<n:
            exDirs.append(string.strip(fin.readline(), "\n"))
            ed+=1
        while nd<m:
            newDirs.append(string.strip(fin.readline(), "\n"))
            nd+=1
        fout.write("Case #"+str(p)+": "+ str(countMD(exDirs, newDirs))+ "\n")
        p+=1
        

runRC()
