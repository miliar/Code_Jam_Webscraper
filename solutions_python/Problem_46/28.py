
def wf(fileName,ls):
    f = open(fileName,'w')
    for i,l in enumerate(ls):
        f.write('Case #%d: %s\n'%(i+1,l))

def minSwap(ls):
    minMove = 0
    lsMax = []    
    for l in ls:
        m = 0
        for i,j in enumerate(l):
            if j=='1':
                m=i
        print m,l
        lsMax.append(m)
        
    for i in range(len(lsMax)):
        if lsMax[i]>i:
            for j in range(i+1,len(lsMax)):
                if lsMax[j]<=i:
                    for k in range(j,i,-1):
                        t = lsMax[k]
                        lsMax[k] = lsMax[k-1]
                        lsMax[k-1] = t
                        minMove += 1
                    break
            
    return minMove

filename = 'Sample.in'
filename = 'A-small-attempt0.in'
filename = 'A-large.in'
f = open(filename)
contents = f.readlines()
s =contents[0].strip()
Cases = int(s)
print Cases
lsResult = []
current = 1
for count in range(Cases):
    print count,'\t:',contents[current]    
    n = int(contents[current])    
    current += 1
    
    ls = contents[current:current+n]
            
    lsResult.append( minSwap(ls) )
    
    current += n
    
    

#print lsResult

    
wf(filename.split('.')[0]+'.out',lsResult)
