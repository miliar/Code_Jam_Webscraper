f=open("plb.txt","r")
g=open("ans.txt","w+")
def ch(s,a):
    cnt=0
    while(len(s)!=0):
        if(s[0]=="+"):
            s=s[1:]
        else:
            if(len(s)<a):
                return -1
            for i in range(a):
                if(s[i]=="+"):
                    s=s[:i]+"-"+s[i+1:]
                elif(s[i]=="-"):
                    s=s[:i]+"+"+s[i+1:]
            cnt=cnt+1
    return cnt
        
a=int(f.readline())
for i in range(a):
    b=f.readline().split()
    c=b[0]
    d=int(b[1])
    ans=ch(c,d)
    if(ans==-1):
        print("Case #%d: IMPOSSIBLE" %(i+1))
    else:
        print("Case #%d: %d" %((i+1),ans))    
