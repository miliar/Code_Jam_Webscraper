f = open('A-small-attempt1.in', 'r')
out=open('out.txt', 'w')
cases=f.readline()
i=0
while i<cases:
        cards1 = [] 
        cards2=[]
        result=[]
        line = f.readline()
        if not line: break
        row1=line
        for x in range(0, 4):
                cards1.append(f.readline().split())
        row2=f.readline()
        for x in range(0, 4):
                cards2.append(f.readline().split())
        for x in range(0, 4):
                for y in range(0, 4):
                        if(cards1[int(row1)-1][x]==cards2[int(row2)-1][y]):
                                result.append(cards1[int(row1)-1][x])

        if(len(result)==0):
                out.write("Case #"+str(i+1)+": Volunteer cheated!\n")
        elif(len(result)==1):
                out.write("Case #"+str(i+1)+": "+str(int(result[0]))+"\n") 
        else:
                out.write("Case #"+str(i+1)+": Bad magician!\n")
        i+=1
out.close()
