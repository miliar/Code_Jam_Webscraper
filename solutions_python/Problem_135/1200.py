import sys;
input_from_file=True
fout=open("G:/o.txt","w")
if input_from_file:
    f=open("C:/ab.txt","r")
else:
    f=sys.stdin
    
t=int(f.readline())
for i in range(t):
    data=[]
    data1=[]
    x=int(f.readline())
    x=x-1
    for j in range(4):
        s=f.readline()
        data.append(map(int,s.split()))
    y=int(f.readline())
    y=y-1
    for j in range(4):
        s=f.readline()
        data1.append(map(int,s.split()))
    r=[j for j in data[x] if j in data1[y]]
    l=len(r)
    #print r
    if l==1:
        output="Case #" + str(i+1) + ": "+ str(r[0]) + "\n"
    elif l==0:
         output="Case #"+ str(i+1) + ": Volunteer cheated!\n"
    else:
         output="Case #"+ str(i+1) + ": Bad magician!\n"
    fout.write(output)
fout.close()
    

        
                     
