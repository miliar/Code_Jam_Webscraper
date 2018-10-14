from decimal import Decimal
finput = open('cookie\input.in', 'r')
foutput=open('cookie\output.in','w')
str=finput.readline()


def fun(buytime,c,f,x):
    time=0
    f1=2
    for i in range(buytime):
        time+=c*1.0/f1
        f1+=f
    time+=x*1.0/f1
    return time        
counter=0
while(str):
    str=finput.readline()
    list=str.split(' ')
    
    c=float(list[0])
    f=float(list[1])
    x=float(list[2])
    time=[]
    print "x is",c,f,x
    if(c>x):
        time.append(float(x)*1.0/2)
    else:
        print "in else"
        cookie=2
        buytime=0
        flag=True
        while(flag):
            print "in while",buytime,c,f,x
            temp=fun(buytime,c,f,x)
            print "temp is",temp
            if(len(time)!=0):
                print "temp",min(time),temp
                if(temp>min(time)):
                    flag=False
            buytime+=1
            time.append(temp)
    foutput.write("Case #%d: %.7f\n"%(counter+1,(min(time))))
    print "time is ",min(time)
    counter+=1
        
        






