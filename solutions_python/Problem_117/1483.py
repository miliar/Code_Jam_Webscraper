f = open('B-large.in','r')
amount=int(f.readline())
writefile = open('result','w')
case=1
matrix=[]
result=[]
while amount!=0:
    nm=[int(x) for x in f.readline().split()]
    matrix[:]=[]
    result[:]=[]
    for i in range(nm[0]):
        matrix.append([int(x) for x in f.readline().split()])
    possible='YES'
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]!=max(matrix[i]):
                if matrix[i][j]!=max([x[j] for x in matrix]):
                    possible='NO'
                    break
        if possible=='NO':
            break
    print('Case #'+str(case)+': '+possible)
    writefile.write('Case #'+str(case)+': '+possible+'\n')
    amount-=1
    case+=1
writefile.close()
