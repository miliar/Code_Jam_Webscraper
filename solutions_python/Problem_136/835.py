def readfile(f): 
    data=[]
    lines = f.readlines()
    for line in lines:
        line=line.strip('\n')
        line=line.split(' ')
        line=map(float,line)
        data.append(line),                    
    f.close()
    return data

f=file('B-large.in','r')
data=readfile(f)
f.close()

num=int(data[0][0])
del data[0]
times=[]

for Z in data:
    C=Z[0]
    F=Z[1]
    X=Z[2]
    i=0
    tick=0
    time=0
    while tick==0:
        if (X-C)/(2+i*F)>X/(2+(i+1)*F):
            time+=C/(2+i*F)
            i+=1
        else:
            time+=X/(2+i*F)
            times.append(time)
            tick=1
            
f2=file('B_large_output.in','w')
for i in range(0,num):
    f2.write("Case #%d: %s\n" % (i+1,times[i]))
f2.close()
