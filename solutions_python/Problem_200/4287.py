t= int(raw_input())
a=[]
for i in range(10):
    a.append(i)
for i in range(1,10):
    for j in range(i,10):
        a.append(i*10+j)
for i in range(1,10):
    for j in range(i,10):
        for k in range(j,10):
            a.append(i*100+j*10+k)
m=1

while m<=t:
    f=0
    n=int(raw_input())
    print "Case #"+str(m)+":",
    if n==1000:
        print 999
        m=m+1
        continue
    for i in range(len(a)):
        k=a[i]
        if n<k:
            f=1
            break
        elif n==k:
            f=2
            break    
    if f==1:
        print a[i-1]
    else:
        print a[i]
    m=m+1
