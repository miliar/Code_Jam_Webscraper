f1 = open("B-small-attempt1.in","r")
f2 = open("out.txt","w")

data = f1.readlines()
k = int((data[0].split())[0])
ind=1
for i in range(k):
    dim=data[ind].split()
    ac=int(dim[0])
    aj=int(dim[1])
    ind+=1
    if ac==0:
        if aj<2:
            f2.write("Case #"+str(i+1)+": 2\n")
            ind+=1
        else:
            hrs=data[ind].split()
            aj1=int(hrs[0]),int(hrs[1])
            ind+=1
            hrs=data[ind].split()
            aj2=int(hrs[0]),int(hrs[1])
            ind+=1
            if aj1[0]>aj2[0]:
                aj1,aj2=aj2,aj1
            if aj2[1]-aj1[0]<=720 or aj2[0]-aj1[1]>=720:
                f2.write("Case #"+str(i+1)+": 2\n")
            else:
                f2.write("Case #"+str(i+1)+": 4\n")        
    elif aj==0:
        if ac<2:
            f2.write("Case #"+str(i+1)+": 2\n")
            ind+=1
        else:
            hrs=data[ind].split()
            aj1=int(hrs[0]),int(hrs[1])
            ind+=1
            hrs=data[ind].split()
            aj2=int(hrs[0]),int(hrs[1])
            ind+=1
            if aj1[0]>aj2[0]:
                aj1,aj2=aj2,aj1
            if aj2[1]-aj1[0]<=720 or aj2[0]-aj1[1]>=720:
                f2.write("Case #"+str(i+1)+": 2\n")
            else:
                f2.write("Case #"+str(i+1)+": 4\n")
    else:
        f2.write("Case #"+str(i+1)+": 2\n")
        ind+=2
f1.close()
f2.close()
