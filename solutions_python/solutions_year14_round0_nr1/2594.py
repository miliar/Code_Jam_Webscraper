fin=file('A-small-attempt0.in')
T=int(fin.readline())

solution=[]
for i in range(T):
    y=[]
    for k in range(2):
        x=int(fin.readline())
        for j in range(4):
            xx=fin.readline()
            if(j==x-1):
                y.append(set([int(xxx) for xxx in xx.split()]))
    z=((y[0]&y[1]).pop() if len(y[0]&y[1])==1 else ["Volunteer cheated!","Bad magician!"][int(len(y[0]&y[1])>0)])
    solution.append("Case #%d: %s"%(i+1,z))
fin.close()
fout=file('A-small-attempt0.out','w+')
fout.write("\n".join(solution))
fout.close()