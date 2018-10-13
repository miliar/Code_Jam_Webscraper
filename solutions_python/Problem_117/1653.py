__author__ = 'guoyongzhen'

def process(rows,columns):
    for row in rows:
        if isSame(row):
            continue
        for i in range(len(row)):
            if row[i]=='1':
                if not isSame(columns[i]):
                    return 'NO'
    return 'YES'

def isSame(str):
    return ('1' in str) != ('2' in str)

input=file('B-small-attempt0.in','r')
output=file('B-small-attempt0.out','w')
res=[]
for case in range(int(input.readline())):
    firstLine=input.readline().split(' ')
    N=int(firstLine[0])
    M=int(firstLine[1])
    rows=[]
    columns=[]
    for i in range(N):
        rows.append(input.readline().replace(' ','').rstrip('\n'))
    for i in range(M):
        column=[]
        for j in range(N):
            column.append(rows[j][i])
        columns.append(''.join(column))
    res.append('Case #%s: %s\n'%(case+1,process(rows,columns)))
print res
output.writelines(res)
output.close()
input.close()