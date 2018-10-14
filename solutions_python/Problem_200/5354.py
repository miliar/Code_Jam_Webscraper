t=int(input())

for i in range(t):
    x=int(input())
    
    while x>=1:
        a=[int(i) for i in str(x)]
        
        if((a==sorted(a))):
            
            print("Case #{0}: {1}".format(i+1,x))
            break
        boole=False
        for j in range(len(a)-1):
            if (a[j]==1) and (a[j+1]==0):
                boole=True
        """if(boole):
            x=int('{0}'.format(a[0])+'9'*(len(a)-1))
        else:"""
        x-=1

        
