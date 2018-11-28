f=open(r"A-small-attempt0.in", 'r+')
fo=open(r"hi.out","w")
n=int(f.readline())
j=0
check1=[]
line=[]
line2=[]
count=0
while(j<n):
    case1=int(f.readline())
    line.append(f.readline().rstrip())
    line.append(f.readline().rstrip())
    line.append(f.readline().rstrip())
    line.append(f.readline().rstrip())
    check1=line[case1-1].split()
    case2=int(f.readline())
    line2.append(f.readline().rstrip())
    line2.append(f.readline().rstrip())
    line2.append(f.readline().rstrip())
    line2.append(f.readline().rstrip())
    check2=line2[case2-1].split()
    for i in check1:
        if i in check2:
            count=count+1
            a=int(i)
    if(count>1):
        fo.write("Case #"+str(j+1)+": Bad magician!"+"\n")
    elif(count==0):
        fo.write("Case #"+str(j+1)+": Volunteer cheated!"+"\n")
    elif(count==1):
        fo.write("Case #"+str(j+1)+": "+str(a)+"\n")
    line=[]
    line2=[]
    count=0
    j=j+1
fo.close()
f.close()
