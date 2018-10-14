def change_pancake(s,flp,i):
    while(flp>0):
        if(s[i]=="+"):
            s[i]="-"
        else:
            s[i]="+"
        flp-=1
        i+=1
    return s
    

a=int(input())
for j in range(a):
    b=list(input().split())
    s=list(b[0])
    flp=int(b[1])
    l=len(s)
    counter=0
    for i in range(l):
        if(l-i>=flp):        
            if(s[i]=="-"):
                s=change_pancake(s,flp,i)
                counter+=1
        else:
            if("-" in s):
                print("Case #%d: IMPOSSIBLE"%(j+1))
                break
            else:
                print("Case #%d: %d"%(j+1,counter))
                break
                

