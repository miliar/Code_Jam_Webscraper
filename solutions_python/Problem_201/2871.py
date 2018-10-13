def stalls(n,k):
    if k>=n:
        return 0,0
    index = (n+2)*[0]
    index[0] = 1
    index[n+1] = 1    
    candidates = []
    for i in range(1,n+1):
        candidates.append(i)
    while k > 0:
        #print 'loop',k,index
        
        if len(candidates)== 0:
            return 0,0
        l_s=None
        r_s=None
        best_s = None
        #print 'candidate:',candidates
        for s in candidates:
            l = 0
            r = 0
            while index[s-l-1]==0:
                l+=1
            while index[s+r+1]==0:
                r+=1
            #print s,l,r
            if best_s is None \
            or min(l_s,r_s)<min(l,r) \
            or (min(l_s,r_s)==min(l,r) and max(l_s,r_s)<max(l,r))\
            or (min(l_s,r_s)==min(l,r) and max(l_s,r_s)==max(l,r) and l_s>best_s):
                    best_s = s
                    l_s=l
                    r_s=r
                    #print 'best_s',best_s
        index[best_s]= 1
        candidates.remove(best_s)
        k-=1
    return max(l_s,r_s),min(l_s,r_s)

inputfname ="C-small-1-attempt1.in" #"A-small-practice.in"
outputfname = inputfname+".out"
with open(inputfname,"r") as f:
    lines = f.readlines()
lines2 = [
'5',
'4 2',
'5 2',
'6 2',
'1000 1000',
'1000 1'
]
n = int(lines[0].strip('\n'))
with open(outputfname,"w") as f:
     f.write('')
with open(outputfname,"a") as f:
    for i in range(1,n+1):
        n,k = map(int,lines[i].strip('\n').split(' '))
        #print '----',num
        minn,maxn=stalls(n,k)
        outstring = 'Case #'+str(i)+': '+str(minn)+' '+str(maxn)
        print outstring
        f.write(outstring+"\n")