t=int(raw_input().strip())



def num(s):
    n=len(s)
    a= []
    k=None
    #flag=True
    for i in range(n-1):
        if int(s[i])<=int(s[i+1]):
            a.append(s[i])
        else:
            k=i
            break
    if k!=None:
        last_ind=k
        a.append(str(int(s[k])-1))
        for i in range(k,0,-1):
            if int(a[k]) >= int(a[k-1]):
                continue
            else:
                last_ind = i-1
                a[i-1]=str(int(a[i-1])-1)
        a = a[:last_ind+1]
        for i in range(last_ind+1,n):
            a.append('9')
    else:
        a.append(s[n-1])
    return int(''.join(a))
    

    
        
for i in range(t):
    s=raw_input().strip()
    print 'Case #{}: {}'.format(i+1,num(s))
