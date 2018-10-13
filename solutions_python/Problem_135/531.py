f = open('work.txt.in', 'r')
f1 = open('workout.txt','w')
case=f.readline()
for casecount in range (0,int(case)):
    answer= f.readline()
    for i in range (0,int(answer)-1):
        f.readline()
    row= f.readline().strip()
    for i in range (0,4-int(answer)):
        f.readline()
    answer2= f.readline()
    for i in range (0,int(answer2)-1):
        f.readline()
    row2= f.readline().strip()
    for i in range (0,4-int(answer2)):
        f.readline()
    count=0
    out=0
    row=row.split(' ')
    row2=row2.split(' ')
    for i in row:
        for j in row2:
            if (i==j and i!='' and i!=' '):
                count=count+1
                out=i
    if(count==1):
        f1.write("Case #"+str(int (casecount)+1)+": "+out+"\n")
    elif (count>1):
        f1.write("Case #"+str(int (casecount)+1)+": Bad magician!"+"\n")
    elif(count==0):
        f1.write("Case #"+str(int (casecount)+1)+": Volunteer cheated!"+"\n")
f.close()
f1.close()
        
