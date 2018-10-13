n=int(input().strip())
for o in range(n):
    t=input().strip()
    a=list(t)
    i=0
    while i!=len(a)-1:
        if int(a[i])>int(a[i+1]):
            if i==len(a)-2 and a[i]=='1' and a[i+1]=='0':
                a[i-1]=str(int(a[i-1])-1)
                a[i]='9'
                a[i+1]='9'
                i=0
            else:
                
                a[i]=str(int(a[i])-1)
                for j in range(i+1,len(a)):
                    a[j]='9'
                i=0
        else:
            i=i+1
    w=''.join(a)
    print("Case #",o+1,sep="",end="")
    print(":",int(w))
    
