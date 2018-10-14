inp=open('input.txt', 'rb')
outp=open('output.txt', 'w')
cases=int(inp.readline())
for case in range(0,cases):
    line=inp.readline()
    [n,A,B,C,D,x,y,M] = [int(i) for i in line.split(' ')]
    trees=[]
    X=x
    Y=y
    valid=0
    trees.append([X,Y])
    for i in range(1,n):
        X=(A*X+B)%M
        Y=(C*Y+D)%M
        trees.append([X,Y])
    for i in range(0,len(trees)):
        for j in range(i+1,len(trees)):
            for k in range(j+1,len(trees)):
                """temp=[(trees[i][0]+trees[j][0]+trees[k][0])/3,(trees[i][1]+trees[j][1]+trees[k][1])/3]
                print temp
                if temp in trees:
                    valid=valid+1"""
                if ((trees[i][0]+trees[j][0]+trees[k][0])%3==0 and (trees[i][1]+trees[j][1]+trees[k][1])%3==0):
                    valid=valid+1
    s="Case #"+str(case+1)+": "+str(valid)+"\r\n"
    outp.write(s)
inp.close()
outp.close()
