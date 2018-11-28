'''
Created on 2013/4/13

@author: kaimugen
'''
f=open("B-small-attempt0.in",'r')
caseTotal=f.readline()
caseCount=0
f2=open("output.txt",'w')
print(caseTotal)
while(caseCount<int(caseTotal)):
    caseCount+=1
    lawn=[]
    MaxRow=[]
    MaxColumn=[]
    scope=f.readline().split(' ')
    columnCount=0
    """getLawn"""
    while(columnCount<int(scope[0])):
        columnCount+=1
        temp=f.readline().split('\n')
        lawn.append(temp[0].split(' '))
        #print(scope,lawn[columnCount-1])
        MAX=0
        """Get max row"""
        for i in range(int(scope[1][:-1])):
            if(MAX<=lawn[columnCount-1][i]):
                MAX=lawn[columnCount-1][i]
        #print(MAX)
        MaxRow.append(MAX)
    """Get Max colmun"""
    for i in range(int(scope[1][:-1])):
        MAX=0
        for w in range(int(scope[0])):
            if(MAX<=lawn[w][i]):
                MAX=lawn[w][i]
        MaxColumn.append(MAX)
    check=0
    for i in range(int(scope[0])):
        if(check):
            break
        for w in range(int(scope[1][:-1])):
            if(not(MaxRow[i]==lawn[i][w] or MaxColumn[w]==lawn[i][w])):
                check=1
                break
    if(not check):
        f2.write("Case #%d: YES\n"%(caseCount))
    else:
        f2.write("Case #%d: NO\n"%(caseCount))    
    

    
f.close()
f2.close()
    