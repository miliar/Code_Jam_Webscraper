import re
t=int(input())
for j in range(t):
        x=input()
        h=int(x)
        s=list(map(int,x))
        f=re.search('^(1)+0', x)
        if(f):
                l=len(x)
                l=l-1
                print("Case #%d: "%(j+1),'9'*l)
                continue;
        for i in range(len(s)-1):
                
                if(i==0):
                        if(s[i]>s[i+1]):
                                s[i]=s[i]-1
                                for a in range(i+1,len(s)):
                                               s[a]=9
                                break
                else:
                        if(s[i]>s[i+1] and s[i]!=s[i-1]):
                                s[i]=s[i]-1
                        elif(s[i]>s[i+1]):
                                s[i-1]=s[i-1]-1
                                i=i-1
                        
                                for a in range(i+1,len(s)):
                                               s[a]=9
                                break
                        
        
        d=int(''.join(map(str,s)))
        if(d<h):
                s[len(s)-1]=9
        
        print("Case #%d: "%(j+1),int(''.join(map(str,s))))
                
	
