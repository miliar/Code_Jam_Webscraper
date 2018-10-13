t = int(raw_input())
for i in xrange(t):
    
    n=input()
    n=str(n)
    a = []

    for digit in n:
        a.append (int(digit))
        
    l=len(a)
    
    for j in xrange(l-1):
        if a[j]>a[j+1]:
            a[j]-=1
            temp=j+1
            
            while(temp<l):
                a[temp]=9
                temp+=1
            temp=j
            while(temp>0 and a[temp]<a[temp-1]):
                a[temp]=9
                a[temp-1]-=1
                temp-=1
    
    print "Case #{}: {}".format(i+1,int("".join(map(str,a))))
    
    
    