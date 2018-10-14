fob=open('B-large.in.txt','r')
caseNum=int(fob.readline())
for x in range(0,caseNum):
    data=fob.readline().split()
    C=float(data[0])
    F=float(data[1])
    X=float(data[2])
    total=0
    a=0
    cokispersecond=2
    timetowin=X/2
    timetowinbyfrm=0
    while timetowin>timetowinbyfrm+total:
        timetowin=X/cokispersecond
        
        total=C/cokispersecond
        a=a+total
        cokispersecond=cokispersecond+F
        timetowinbyfrm=X/cokispersecond
    final=timetowin+a-(C/(cokispersecond-F))
    print("Case #"+str(x+1)+": "+str(format(final,'.7f')))
        
        
