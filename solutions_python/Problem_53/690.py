fin=open('A-large.in','r')
fo=open('A-large.out','w')
t=int(fin.readline())
i=0
while i<t:
    i+=1
    s=fin.readline()   
    n,k=map(int,s.split())
    powof2=2**n
    if k%powof2==powof2-1:
        fo.write('Case #%d: ON\n'%(i))
    else:
        fo.write('Case #%d: OFF\n'%(i))
fin.close()
fo.close()

