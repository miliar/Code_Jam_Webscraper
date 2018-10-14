
ff=open("qq.in",'r')
n = int(ff.readline().strip('\n'))
nash=open('finaly.out','w')

j=1
while j <= n:
    test= ff.readline().strip().split()
    c=float(test[0])
    f=float(test[1])
    x=float(test[2])
    rate=2
    co=0
    time=[]
    while x/rate > (c/(rate))+ (x/(rate+f)):
        time.append(c/rate)
        rate=rate+f
    time.append(x/rate)
        
    
    total = 0
        
    for i in time:
        total = total +i

    
    nash.write("Case #"+str(j)+": "+str("%.7f"%total)+"\n" )
    test=[]
    j=j+1

ff.close()
nash.close()

