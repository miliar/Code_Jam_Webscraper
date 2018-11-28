def qwert(a):
    for k in range(len(a)-1):
        if a[k]<=a[k+1]:
            pass
        else:
            a[k]=a[k]-1
            for l in range(k+1,len(a)):
                a[l]=9
    return a            
n=int(input())
for p in range(n):
    t=int(input())
    a=[int(j) for j in str(t)]
    while(True):
        if a==sorted(a):
            b="".join(map(str,a))
            if b[0]=='0':
                print("Case #{}: {}".format(p+1,b[1:]))
                break
            else:
                print("Case #{}: {}".format(p+1,b))
                break
        else:
            qwert(a)