f = open('input.txt','r')
w = open('output.txt','w')
nmax=int(f.readline())
for n in range(0,nmax):
    r1=int(f.readline())-1
    m1=[]
    for m in range(0,4):
        m1.append(f.readline())
    l1=m1[r1].split()
    r2=int(f.readline())-1
    m2=[]
    for m in range(0,4):
        m2.append(f.readline())
    l2=m2[r2].split()
    s=set(l1)&set(l2)
    if len(s)<1:
        a='Volunteer cheated!'
    elif len(s)==1:
        a=list(s)[0]
    else:
        a='Bad magician!'
    w.write('Case #'+str(n+1)+': '+a+'\n')
f.close()
w.close()
