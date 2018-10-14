f1=open("test_cookie","r")
f2=open("writ","w")
l = f1.readlines()
for i in range(0,len(l)):
    l[i]=l[i][:-1]
p=1
for i in range(0,int(l[0])):
    lis = l[p].split(' ')
    p = p+1
    C=float(lis[0])
    F=float(lis[1])
    X=float(lis[2])
    c = 0
    f = 2
    tim1=[0.0,0.0]
    tim2=[0.0,0.0]
    while(1):
        tim2[0] = tim1[0]
        tim1[0] = tim1[0] + C/f
        tim2[1] = X/f
        f = f + F
        t = X/f
        tim1[1] = t
        
        if((tim1[0]+tim1[1])>(tim2[0]+tim2[1])):
            print "Case #"+str(i+1)+": "+str(round((tim2[0]+tim2[1]),7))
            break
f1.close()
f2.close()
        