t=int(raw_input().strip())
for i in xrange(t):
    n=int(raw_input().strip())
    s1=s2=True
    temp=[]
    k=str(n)
    start=0
    for j in xrange(len(k)-1):
        if k[j]==k[j+1] and s2==True:
            start=j
            s2=False
        elif k[j]>k[j+1]:
            k=list(str(int(''.join(k[start:]))-int(''.join(k[start+1:]))))
            s1=False
            break
        elif k[j]<k[j+1]:
            temp.extend(k[start:j+1])
            start=j+1
            s2=True
    if(s1==False):
        temp.extend(list(str(int(''.join(k))-1)))
    else:
        temp.extend(k[start:])
    ans=int(''.join(temp))
    print "Case #{}: {}".format(i+1,ans)
