import psyco
psyco.full()
def tobase2(nb):
    rst=[]
    while nb>0:
        if nb&1>0:
            rst.append('1')
        else:
            rst.append('0')
        nb=nb>>1
    rst.append('0')
    return rst
print 'starting'
fin=file('a.in')
fout=file('a.out','w')
T=int(fin.readline().strip())
for t in range(T):
    N,K=[int(x) for x in fin.readline().strip().split()]
    str_k=tobase2(K);
    #print str_k
    if len(str_k)>=N:
        state='ON'
        for n in range(N):
            if str_k[n]=='0':
                state='OFF'
                break
    else:
        state='OFF'
    fout.write('Case #%d: %s\n'%(t+1,state))
fout.close()
print 'ok'