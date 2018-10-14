#!/usr/bin/python

def createDic():
    d={}
    for h in range(24):
        for m in  range(60):
            str = "%i%02i" % (h,m)
            d[int(str)]=[]
    return d
def add(time,T):
    s = "%04i" % (time)
    m = int(s[-2:])
    h= int(s[:-2])
    mnew = (m+T)%60
    hnew = h+ (m+T)/60
    str = "%i%02i" % (hnew,mnew)
    return int(str)

for case in range(input()):
    T = raw_input()
    T = int(T)
    NA,NB= raw_input().split()
    ATable={}
    BTable={}
    readyA=0
    readyB=0
    trainA=0
    trainB=0

    for na in range(int(NA)):
        depart, arrive = raw_input().split()
        depart =depart.split(':')[0]+depart.split(':')[1]
        depart = int(depart)
        arrive =arrive.split(':')[0]+arrive.split(':')[1]
        arrive = int(arrive)

        if depart in ATable.keys():
            ATable[depart].append(add(arrive,T))
        else:
            ATable[depart]=[]
            ATable[depart].append(add(arrive,T))

    for na in range(int(NB)):
        depart, arrive = raw_input().split()
        depart =depart.split(':')[0]+depart.split(':')[1]
        depart = int(depart)
        arrive =arrive.split(':')[0]+arrive.split(':')[1]
        arrive = int(arrive)
        if depart in BTable.keys():
            BTable[depart].append(add(arrive,T))
        else:
            BTable[depart]=[]
            BTable[depart].append(add(arrive,T))

    d= createDic();
    for t in d.keys():
        if t in ATable.keys():
            for i in ATable[t]:
                d[t].append("DA")
                d[i].append("AB")
                
        if t in BTable.keys():
            for i in BTable[t]:
                d[t].append("DB")
                d[i].append("AA")

    for t in  d.keys():
        if "AA" in d[t]:
            readyA+=d[t].count('AA')
        if "AB" in d[t]:
            readyB+=d[t].count('AB')
        if "DA" in d[t]:
            if readyA<=d[t].count('DA'):
                trainA+= d[t].count('DA') - readyA
                readyA=0
            else:
                readyA-=d[t].count('DA')
        if "DB" in d[t]:
            if readyB<=d[t].count('DB'):
                trainB+=d[t].count('DB')-readyB
                readyB=0
            else:
                readyB-=d[t].count('DB')

        
    print "Case #%i: %i %i" % (case+1,trainA,trainB)
