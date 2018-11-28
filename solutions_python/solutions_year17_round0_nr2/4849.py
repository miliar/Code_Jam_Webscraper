T= input()
res=[]

for i in range(T):
    n=input()
    if n<10:
        res.append(n)
    else:    
        for i in range(n,0,-1):
            if i<10:
                res.append(i)
                break

            a=str(i)
            ans=0
            for j in range(len(a)-1):
                if int(a[j+1])<int(a[j]):
                    ans=1
                    break
            if ans==0:
                res.append(i)
                break


for i in range(T):
    print 'Case #'+str(i+1)+': '+str(res[i])            
                    
                
        
        
