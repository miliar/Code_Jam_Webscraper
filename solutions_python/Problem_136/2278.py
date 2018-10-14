file=open("B-large.in",'r')
output=open("q2answerlarg.out",'w')
temp1=file.readlines()
temp2=[]
for i in temp1:
    temp2.append(i.split())
temp3=temp2.pop(0)
NumOfTests=int(temp3.pop(0))
count=0
while count<NumOfTests:
    temp4=temp2.pop(0)
    c=float(temp4.pop(0))
    f=float(temp4.pop(0))
    x=float(temp4.pop(0))
    r=2
    t=0
    k=0
    T=x/r
    arr=[]
    while x/r > (c/(r))+ (x/(r+f)):
        arr.append(c/r)
        r=r+f
    arr.append(x/r)
        
    final = 0
        
    for i in arr:
        final = final +i

    final='%.7f' %final

    #print(final)
    output.writelines("Case #"+str(count+1)+": "+final+"\n")
    count=count+1
file.close()
output.close()
