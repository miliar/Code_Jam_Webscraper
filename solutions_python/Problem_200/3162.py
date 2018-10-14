def tidy(n):
    ns=str(n)
    ii=0
    k=len(ns)
    for i in range(k-1):
        if(int(ns[i]) <= int(ns[i+1])):
            ii=i+1
        else:
            break
    if ii==k-1:
        return n
    else:
        i=ii
        while(ns[i]==ns[i-1] and ii>0):
            i=i-1
        r='%s%s%s' %(ns[:i],int(ns[i])-1,len(ns[i+1:])*'9')
        return int(r)


if __name__ == "__main__":
    n=int(raw_input())
    for e in range(1,n+1):
        t=int(raw_input())
        print "Case #%s: %s" %(e , tidy(t))

