def honest(n,k):
    if len(n)==0:
        return 0
    nl=0
    nr=len(n)-1
    kl=0
    kr=len(k)-1
    s=0
    while nr-nl>-1:
        if n[nr]>k[kr]:
            s+=1
            nr-=1
            kl+=1
        else:
            nr-=1
            kr-=1
    return s

def deceit(n,k):
    s=0
    i=0
    j=0
    while i<len(k):
        if n[i]>k[j]:
            s+=1
            i+=1
            j+=1
        else:
            i+=1
    return s


with open('/home/gauravjs/Documents/Google Code Jam/2014Q/inputfile4l','r') as f:
    cases=int(f.readline())
    lines=f.readlines()
for i in range(cases):
    matches=int(lines[i*3].strip())
    naomi=[float(x) for x in lines[i*3+1].strip().split(' ')]
    ken=[float(x) for x in lines[i*3+2].strip().split(' ')]
    naomi.sort()
    ken.sort()

    print 'Case #'+str((i+1))+':',deceit(naomi,ken),honest(naomi, ken)
