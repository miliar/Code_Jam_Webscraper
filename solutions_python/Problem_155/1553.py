cases=int(input())
out=[];shyLst=[]
for i in range (0,cases):
    line=str(input())
    line=line.split()
    line=list(map(str,line))#for convert string list to int list
    maxShyLevel=line[0] #line[1] =""
    shyLst=list(str(line[1]))
    shyLst=list(map(int,shyLst))
    count=shyLst.pop(0)
    
    num=0;extr=0;level=1;
    while(shyLst):
        if shyLst[num]>=1:
            if level<=count:
                count+=shyLst[num]
                shyLst.pop(0)
                level+=1
            else:
                extr=extr+(level-count)
                count=level
                
            
        elif shyLst[num]==0:
            shyLst.pop(0)
            level+=1
    out.append(extr)
            
            
            
            
    
    

out.reverse()
lenprint=0
while len(out):
    lenprint+=1
    print("Case #",end="")
    print(lenprint,end="")
    print(": ",end="")
    print(out.pop())
    
