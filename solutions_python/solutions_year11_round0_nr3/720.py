
fl = open('C-large.in','r')
case=int(fl.readline())
def add(l):
    f=list(l[0])
    for i in l[1:]:
        r=list(i)
        for h,k in enumerate(r):
            if f[h]=='1' and k=='1':
                f[h]='0'
            else:
                f[h]=str(int(k)+int(f[h]))
    return ''.join(f) 
            
for j in range(case):
    z=fl.readline()
    z=fl.readline().split()
    for i,f in enumerate(z):
        z[i]=int(f)
    z.sort()
    sex=sum(z[1:])
    for i,f in enumerate(z):
        z[i]=bin(f)[2:]
    m=0
    for i in z:
        if len(i)>m:
            m=len(i)
    for i,f in enumerate(z):
        while len(f)<m:
            z[i]='0'+z[i]
            f=z[i]
    if int(add(z))!=0:
        a='NO'
    else:
        '''
        for i in range(len(z)):
            try:
                if add(z[:i])==add(z[i:]):
#                    a=add(z[:i])
#                    a=int(a,2)
                    for w,x in enumerate(z):
                        z[w]=int(x,2)
                    if sum(z[:i])>sum(z[i:]):
                        a=sum(z[:i])
#                        print z[:i]
                    else:
                        a=sum(z[i:])
#                        print z[i:]
                        
            except: pass
        '''
        a=sex
    print "Case #%d:"%(j+1),a
