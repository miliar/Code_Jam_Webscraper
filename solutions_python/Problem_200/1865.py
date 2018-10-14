testCases=int(input())
lis=[None]*testCases
for i in range(testCases):
    input1=input()
    
    temparr=list(str(input1))
    
    for j in range(len(temparr)-1,0,-1):
        
        if(int(temparr[j-1])<=int(temparr[j])):
            continue
        else:
            temparr[j-1]=""+str(int(temparr[j-1])-1)
            for k in range(j,len(temparr)):
                temparr[k]='9';
            
            
        
        
        
           
            
    temparr1="".join(temparr);
    lis[i]=int(temparr1)  ;  
     
            
for n in range(len(lis)):
    stre="Case #"+str((n+1))
    stre=str(stre)+": "+str(lis[n])
    print(stre)
    
    
    