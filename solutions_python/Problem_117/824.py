inp=open('B-large.in','r')
n=int(inp.readline().rstrip('\n'))
for counter in range(1,n+1):
    size=inp.readline().rstrip('\n').split(' ')
    size[0]=int(size[0])
    size[1]=int(size[1])
    lawn=[[None for _ in range(size[1])] for _ in range(size[0])]
    for i in range(size[0]):
        line=inp.readline().rstrip('\n').split(' ')
        j=0
        for letter in line:
            lawn[i][j]=int(letter)
            j+=1
    result=1
    for i in range(size[0]):
        for j in range(size[1]):
            
            if max(lawn[i])==lawn[i][j]:
                continue
            else:
                vert=[]
                for k in range(size[0]):
                    vert.append(lawn[k][j])  
                                  
                if max(vert)==lawn[i][j]:                    
                    continue
                else:
                    
                    result=0
    if result==1:
        res='YES'
    else:
        res='NO'
    print 'Case #%d: %s'%(counter,res)
            
    


