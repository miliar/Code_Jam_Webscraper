n=int(input());
for j in range(0,n):
    x=int(input());
    w=1;
    x1=str(x);
    l1=len(x1);
    if(l1>1):
        while(w==1):
            d=1;
            s=str(x);
            l=len(s);
            for i in range(0,(l-1)):
                if(int(s[i])>int(s[i+1])):
                    d=0;
            if(d==0):
                x=x-1;
            if(d==1):
                w=2;
        print("Case #"+str(j+1)+": "+str(x));
    if(l1==1):
        print("Case #"+str(j+1)+": "+str(x));
            
                    
