t=int(input())
c=0
for i in range(t):
    c=0
    s=list(input().split(" "))
    #print(s)
    d=s[0]
    m=int(s[1])
    d=list(d)
    for k in range(len(d)):
        #print(d)
        if d[k]=='-':
            if k+m<=len(d):
                c=c+1
                #print(c)
                #print(k)
                for f in range(k,k+m):
                    if d[f]=='-':
                        d[f]='+'
                    else:
                        d[f]='-'
    if d.count('-')==0:
        print("Case #",i+1,sep="",end="")
        print(":",c,sep=" ")
    else:
        print("Case #",i+1,sep="",end="")
        #print(":",c,sep=" ")
        print(":","IMPOSSIBLE",sep=" ")
            
    
