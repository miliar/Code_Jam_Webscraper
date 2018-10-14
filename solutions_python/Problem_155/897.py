lines=[]
file1=open('A-large.in')
for line in file1:
    lines.append(line)
file1.close

T=int(lines[0])
ctr=1
f=open('Output.out','w')
while ctr<=T:
    Smax,S=lines[ctr].split()
    Smax=int(Smax)
    Array=[int(x) for x in S]
    count=0
    need=0
    for i in range(Smax+1):
        if Array[i]>0 or count>i:
            count+=Array[i]
        else:
            count+=1
            need+=1
    f.write("Case #%d: %d" %(ctr,need))
    ctr+=1
    if ctr<=T:
        f.write("\n")
f.close()
