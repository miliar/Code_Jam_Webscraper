(input,out)=(open("in","r"),open("out","w"))
cases=int(input.readline())

for s in xrange(cases):
    out.write('Case #%s: '% (s+1).__str__())
    lin=input.readline().strip().split(' ')
    (n,l,h)=[int(x) for x in lin]
    lin=input.readline().strip().split(' ')
    line=[int(x) for x in lin]
    L_R=xrange(l,h+1)
    nums=[]
    ok=False
    for i in L_R:
        res=sum([(j%i)*(i%j) for j in line])
        if res==0:
            out.write('%d\n'% i)
            ok=True
            break
    if ok==False:
        out.write('NO\n')



