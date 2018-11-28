import fileinput
outr=open('out.txt','w')
l=[]
for line in fileinput.input('B-large.in'):
    l.append(int(line))
r=l[0]
for i in range(1,r+1):
    d=l[i]
    if(d<=9):
        outr.write('Case #%d: %d\n'%(i,l[i]))
        continue
    f=0
    while(True):
        r=d%10
        c=0
        dd=d
        while(d!=0):
            d=d/10
            if(d%10>r):
                c+=1
                x=d%10l
                break
            r=d%10
        if(c==0):
            outr.write('Case #%d: %d\n'%(i,dd))
            break
        else:
            d=dd
            x=(d/(10**f))%10
            d=d+(9-x)*10**f-10**(f+1)
            f=f+1
outr.close()

