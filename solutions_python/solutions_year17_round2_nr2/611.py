rnd="p17R1B"
pb="B"
size="small-attempt1"
fin=open("C:\F\workspace\Euler\EulerProject\GCJam\%s\%s-%s.in"%(rnd,pb,size),'r')
fout=open("C:\F\workspace\Euler\EulerProject\GCJam\%s\%s-%s.out"%(rnd,pb,size),'w')

T=int(fin.readline())
#print T
for i in range(1,T+1):
    n,r,o,y,g,b,v=fin.readline().strip().split()
    N,R,O,Y,G,B,V=int(n),int(r),int(o),int(y),int(g),int(b),int(v)
    if R+O+Y+B+G+V != N:
        print i,R+O+Y+B+G+V,N 
        exit()
        
    res=[]
    counts={"R":R,"O":O,"Y":Y,"G":G,"B":B,"V":V}
    
    next_={"R":("Y","G","B"),
          "O":("G","B","V"),
          "Y":("B","V","R"),
          "G":("V","R","O"),
          "B":("R","O","Y"),
          "V":("O","Y","G")}
    
    nextcolors=next_.keys()
    prioritycolor=""
    while sum([counts[k] for k in counts])>0:
        nextcolorcandidates=[kk for kk in nextcolors if counts[kk]==max([counts[k] for k in nextcolors])]
        maxnextcolor = nextcolorcandidates[0] if prioritycolor not in nextcolorcandidates else prioritycolor
        if prioritycolor=="":
            prioritycolor=maxnextcolor
        if counts[maxnextcolor] == 0:
            res="IMPOSSIBLE"
            break
        res.append(maxnextcolor)
        counts[maxnextcolor]-=1
        nextcolors=next_[maxnextcolor]

    res="".join(res)
    if res[0]==res[-1]:
        res="IMPOSSIBLE"
                
    line="Case #%d: %s" % (i, res)
    print line
    fout.write(line+"\n")
fout.close()