fp=open('B-small-attempt3.in','r')
fw=open('CB-small.out','w')
N=int(fp.readline())
for i in range(1,N+1):
    slist=fp.readline().split()
    a=int(slist[0])
    b=int(slist[1])
    c=int(slist[2])
    ret=0
    for q in range(0,a):
        ii=int(slist[3+q])
        if ii>c and (ii/3>=c or (int((ii)/3)+1==c and (ii%3==2)) or (int((ii)/3)+1==c and (ii%3==1))):
            ret+=1
        elif ii>c and (int(ii/3)+1==c or (int((ii)/3)+2==c and (ii%3==2))):
            b-=1
            if b>-1:
                ret+=1
        elif (ii==0 and c==0) or (ii==1 and c==1):
            ret+=1
    print(ret)
    fw.write("Case #"+str(i)+": "+str(ret))
    fw.write('\n')
fw.close()
