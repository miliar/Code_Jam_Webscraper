def timetominutes(s):
    t=s.split(':')
    return int(t[0])*60+int(t[1])

f=open("B-large.in",'r')
w=open("train-out.txt",'w')
s=f.read().split('\n')
n=int(s.pop(0))
for k in range(n):
    t=int(s.pop(0))
    nanb=s.pop(0).split(' ')
    na,nb=int(nanb[0]),int(nanb[1])
    lna=[]
    lnb=[]
    for c in range(na):
        i=s.pop(0).split(" ")
        lna.append([timetominutes(i[0]),timetominutes(i[1])+t,1])
    for c in range(nb):
        i=s.pop(0).split(" ")
        lnb.append([timetominutes(i[0]),timetominutes(i[1])+t,1])
    lna.sort()
    lnb.sort()
    for i in lna:
        for j in lnb:
            if i[1]<=j[0] and j[2]!=0:
                j[2]=0
                break
    for i in lnb:
        for j in lna:
            if i[1]<=j[0] and j[2]!=0:
                j[2]=0
                break
    a=0
    for i in lna:
        a+=i[2]
    b=0
    for i in lnb:
        b+=i[2]
    w.write('Case #'+str(k+1)+': '+str(a)+' '+str(b)+'\n')
w.close()
f.close()
