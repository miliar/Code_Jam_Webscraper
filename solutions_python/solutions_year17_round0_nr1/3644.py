t=int(input())
for t0 in range(1,t+1):
    s,k=str(input()).split(' ')
    k=int(k)
    count=0
    if '-' not in s[:]:
        print("Case #"+str(t0)+": 0")
    else:
        for i in range(len(s[:])):
            if(s[:][i]=='-' and (i+k)<=len(s[:])):
                count+=1
                for j in range(k):                    
                    if(s[:][i+j]=='-'):
                        s=s[:i+j]+'+'+s[i+j+1:]
                    else: s=s[:i+j]+'-'+s[i+j+1:]
                    
                        
        if '-' in s[:]:
            print("Case #"+str(t0)+": IMPOSSIBLE")
        else:
            print("Case #"+str(t0)+": "+str(count))
            
            
        
        

    
    
    
    
