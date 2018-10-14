def readfile(f): 
    data=[]
    lines = f.readlines()
    for line in lines:
        line=line.strip('\n')
        line=line.split(' ')
        line=map(int,line)
        data.append(line),                    
    f.close()
    return data

f=file('A-small-attempt0.in','r')
data=readfile(f)
f.close()

num=int(data[0][0])
del data[0]
labels=[]

for n in range(0,num):
    x1=data[10*n][0]-1
    x2=data[10*n+5][0]-1
    card1=data[10*n+1:10*n+5]
    card2=data[10*n+6:10*n+10]
    row1=card1[x1]
    row2=card2[x2]
    count=0
    for x in row1:
        for y in row2:
            if y==x:
                number=y
                count+=1
    if count==1:
        labels.append(str(number)+'\n')
    elif count==0:
        labels.append('Volunteer cheated!\n')
    else:
        labels.append('Bad magician!\n')
    
f2=file('A_small_output.in','w')
for i in range(0,num):
    f2.write("Case #"+str(i+1)+": "+labels[i])
f2.close()
