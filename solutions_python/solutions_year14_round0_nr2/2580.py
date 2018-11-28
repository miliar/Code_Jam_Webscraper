fo = open("B-large.in")
fo2 = open("output.txt", mode='w')
output=[]
tests = eval(fo.readline())
for case in range(1,tests+1):
    text=fo.readline().split()
    C=eval(text[0])
    F=eval(text[1])
    X=eval(text[2])

    money=0
    time=0
    farms=0

    while(True):
        t1=(X-money)/(2+farms*F)
        t2=(X-money)/(2+(farms+1)*F) + C/(2+farms*F)
        if(t1<t2):
            output.append("Case #"+str(case)+": "+str(t1+time)+"\n")
            break;
        else:
            time+=C/(2+farms*F)
            farms+=1
fo2.writelines(output)
print("done")


