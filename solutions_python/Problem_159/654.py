ans=""
for i in range(int(raw_input())):
    n=int(raw_input())
    a=map(int,raw_input().split())
    j=0
    c=0
    while j+1<len(a):
        if a[j]>a[j+1]:
            c=c+a[j]-a[j+1]
        j=j+1
    b=a[::-1]
    d=0
    diff=a[0]-a[1]
    kk=0
    while kk<len(a)-1:
        difft=a[kk]-a[kk+1]
        
        if difft>diff:
            diff=difft
        #print diff    
        kk=kk+1            
    truerate=diff
    #print truerate
    k=0
    while k<len(a)-1:
        if a[k]<=truerate:
            d=d+a[k]
        else:
            d=d+truerate
        k=k+1    
    ans=ans+"Case #"+str(i+1)+": "+str(c)+" "+str(d)+"\n"
print ans    
    
