def go(r,k,n,g):
    cyclerounds=0
    cycleeuro=0
    euro=0
    gpos=0
    gset=set([0])
    while r:
        
        runk=k
        numg=0
        while g[gpos]<=runk and numg<n:            

            cycleeuro+=g[gpos]
            euro+=g[gpos]
            runk-=g[gpos]

            gpos=(gpos+1)%n
            numg+=1
            
        

        cyclerounds+=1
        r-=1
##        if gpos in gset:
##            if r>cyclerounds:
##                cycles=r/cyclerounds
##                r-=cycles*cyclerounds
##                euro+=cycles*cycleeuro
##            
##        else:
##            gset.add(gpos)
    return euro


infile=open('in')
outfile=open('out.txt','w')
cases=int(infile.readline())
for c in range(cases):
    r,k,n=[int(x) for x in infile.readline().split()]
    g=[int(x) for x in infile.readline().split()]
    outfile.write('Case #%d: %d\n'%(c+1,go(r,k,n,g)))

infile.close()
outfile.close()
        
