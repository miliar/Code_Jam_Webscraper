def fill(inp):
    temp=int(inp.read(2))
    inp.read(1)
    temp=60*temp+int(inp.read(2))
    inp.read(1)
    temp2=int(inp.read(2))
    inp.read(1)
    temp2=60*temp2+int(inp.read(2))+delay
    return [temp,temp2]

def update(trains, total1, total2, temp1, temp2):
    trains=trains+1
    current=temp1[0][1]
    del temp1[0]
    total1=total1-1
    switch=0
    while (current!=0):
        if switch==0:
            for train in temp2:
                if current<=train[0]:
                    current=train[1]
                    temp2.remove(train)
                    total2=total2-1
                    break
            else:
                current=0
            switch=1
        else:
            for train in temp1:
                if current<=train[0]:
                    current=train[1]
                    temp1.remove(train)
                    total1=total1-1
                    break
            else:
                current=0
            switch=0
    return [trains,total1,total2,temp1,temp2]
    

inp=open('D:\in.txt', 'rb')
output=open('D:\out.txt','w')
cases=int(inp.readline())
for case in range(0,cases):
    tempa=[]
    tempb=[]
    trainsa=0
    trainsb=0
    delay=int(inp.readline())
    counts=inp.readline()
    (na,waste,nb)=counts.partition(' ')
    na=int(na)
    nb=int(nb)
    for i in range(0,na):
        tempa.append(fill(inp))
        inp.readline()
    for i in range(0,nb):
        tempb.append(fill(inp))
        inp.readline()
    tempa.sort()
    tempb.sort()
    '''print 'TempA='
    print tempa
    print 'TempB='
    print tempb
    print 'na='
    print na
    print 'nb='
    print nb
    print '------------------------------------------------------'
    '''
    while (na>0 or nb>0):
        if na==0:
            trainsb=trainsb+len(tempb)
            nb=0
            tempb=[]
        elif nb==0:
            trainsa=trainsa+len(tempa)
            na=0
            tempa=[]
        elif tempa[0][0]<tempb[0][0]:
            [trainsa, na, nb, tempa, tempb]=update(trainsa, na, nb, tempa, tempb)            
        elif tempa[0][0]>tempb[0][0]:
            [trainsb, nb, na, tempb, tempa]=update(trainsb, nb, na, tempb, tempa)
        elif tempa[0][0]==tempb[0][0]:
            if tempa[0][1]<tempb[0][1]:
                [trainsa, na, nb, tempa, tempb]=update(trainsa, na, nb, tempa, tempb)
            else:
                [trainsb, nb, na, tempb, tempa]=update(trainsb, nb, na, tempb, tempa)
        '''print 'TempA='
        print tempa
        print 'TempB='
        print tempb
        print 'na='
        print na
        print 'nb='
        print nb
        print '------------------------------------------------------'
        '''        
    string='Case #'+str(case+1)+': '+str(trainsa)+' '+str(trainsb)+'\r\n'
    output.write(string)
inp.close()
output.close()
