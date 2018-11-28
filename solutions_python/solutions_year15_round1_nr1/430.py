def go():
    f=open('1.in')
    c=int(f.readline())
    for case in range(1,c+1):        
        print 'Case #%d:'%case,
        f.readline()
        print solve(f.readline())
    f.close()

    

def solve(s):
    l=[int(x) for x in s.split()]
    rate=max([l[x]-l[x+1] for x in range(len(l)-1)])
    a,b=0,0
    for x in range(len(l)-1):
        if  l[x]>l[x+1]:
            a+=l[x]-l[x+1]
        if l[x]:
            if l[x]<rate:
                b+=l[x]
            else:
                b+=rate
    return str(a)+' '+str(b)




