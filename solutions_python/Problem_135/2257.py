inf=open("A-small-attempt1.in","r")
outf=open("good.txt","w")
cases=int(inf.readline())

for absdf in range (cases):
    row1=int(inf.readline())
    grid1=[]
    for i in range (4):
        grid1.append(list(map(int,inf.readline().strip().split())))
    grid2=[]
    row2=int(inf.readline())
    for i in range (4):
        grid2.append(list(map(int,inf.readline().strip().split())))

    count=0;
    ans=-1;
    for a in grid1[row1-1]:
        if a in grid2[row2-1]:
            count+=1;
            ans=a;
    outf.write("Case #"+str(absdf+1)+": ")
    if count==0:
        outf.write("Volunteer cheated!"+"\n")
    elif count==1:
        outf.write(str(ans)+"\n")
    else:
        outf.write("Bad magician!"+"\n")

outf.close()
