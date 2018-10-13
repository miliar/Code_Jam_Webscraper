f=open(r"1a.in", 'r+')
fo=open(r"1a.out","w")
n=int(f.readline())
j=0
check1=[]
l=[]
l2=[]
c=0
while(j<n):
    case1=int(f.readline())
    l.append(f.readline().rstrip())
    l.append(f.readline().rstrip())
    l.append(f.readline().rstrip())
    l.append(f.readline().rstrip())
    check1=l[case1-1].split()
    case2=int(f.readline())
    l2.append(f.readline().rstrip())
    l2.append(f.readline().rstrip())
    l2.append(f.readline().rstrip())
    l2.append(f.readline().rstrip())
    check2=l2[case2-1].split()
    for i in check1:
        if i in check2:
            c=c+1
            a=int(i)
    if(c>1):
        fo.write("Case #"+str(j+1)+": Bad magician!"+"\n")
    elif(c==0):
        fo.write("Case #"+str(j+1)+": Volunteer cheated!"+"\n")
    elif(c==1):
        fo.write("Case #"+str(j+1)+": "+str(a)+"\n")
    l=[]
    l2=[]
    c=0
    j=j+1
fo.close()
f.close()
