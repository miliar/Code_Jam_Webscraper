class Time:
    def __init__(self,*arg):
        self.hour=arg[0]
        self.min=arg[1]
    def __cmp__(self,other):
        if self.hour>other.hour:return 1
        elif self.hour==other.hour:
            if self.min>other.min:return 1
            elif self.min==other.min:return 0
            else:return -1
        else:return -1

f=file('B-small-attempt4.in','r')
o=file('out','w')
l=f.readlines()
case_count=int(l[0])
l=l[1:]
for i in range(1,case_count+1):
    wait=int(l[0])
    dlen=l[1].split(' ')
    alen=int(dlen[0])
    blen=int(dlen[1])
    atimes=[]
    atimee=[]
    btimes=[]
    btimee=[]
    for j in range(2,alen+2):
        during=l[j].split(' ')
        h,m=during[0].split(':')
        atimes.append(Time(int(h),int(m)))
        h,m=during[1].split(':')
        atimee.append(Time(int(h),int(m)+wait))
    for j in range(alen+2,alen+2+blen):
        during=l[j].split(' ')
        h,m=during[0].split(':')
        btimes.append(Time(int(h),int(m)))
        h,m=during[1].split(':')
        btimee.append(Time(int(h),int(m)+wait))
    l=l[alen+2+blen:]
    btimes_cp=list(btimes)    
    for ate in atimee:
        mint=Time(24,0)
        for bts in btimes_cp:
            if bts >= ate and bts < mint:
                mint=bts
        if mint.hour<24:btimes_cp.remove(mint)
    atimes_cp=list(atimes)  
    for bte in btimee:
        mint=Time(24,0)
        for ats in atimes_cp:
            if ats >= bte and ats < mint:
                mint=ats
        if mint.hour<24:atimes_cp.remove(mint)     
    o.write('Case #'+str(i)+': '+str(len(atimes_cp))+' '+str(len(btimes_cp))+'\n')
f.close()
o.close()