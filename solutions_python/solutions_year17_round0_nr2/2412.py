t = int(input())
for a in range(t):
    x = int(input())
    while True:
        s = str(x);
        f = 0;
        if(len(s))==1:
           break;
        for i in range(len(s)-1):
            if(s[i]>s[i+1]):
                f = 1;
                break;
        if f ==1:
            j = len(s)-1;
            n = len(s);
            while(j>0):
               if(s[j]<s[j-1]):
                   xx = s[:j-1]+str(int(s[j-1])-1)+'9'*(n-j)
                   #print j,s[:j-1],str(int(s[j-1])-1),(n-j),xx,j;
                   
                   break;
               j-=1;
            x = int(xx);
            
        else:
            break;
    print "Case #"+str(a+1)+":",x;
