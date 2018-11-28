t=int(input())
bigmatrix=[]
select=[]
for i in range(0,t*2):
    matrix=[]
    l1=input()
    select.append(int(l1))
    for k in range(4):
        line=input()
        values=line.split()
        row=[int(value) for value in values]
        matrix.append(row)
    bigmatrix.append(matrix)
k=0
for i in range(0,t*2,2):
    matrix=bigmatrix[i]
    matrix1=bigmatrix[i+1]
    flag=0
    val1=0
    time=0
    for val in matrix[select[i]-1]:
        for var in matrix1[select[i+1]-1]:   
            if val==var:
                flag=1
                val1=val
                time=time+1
    if flag==1 and time<=1:
        print('Case #'+ str(k+1) +': ' +str(val1))
    if flag==1 and time>1:
        print('Case #'+ str(k+1) +': Bad magician!')
    if flag==0 or time==0:
        print('Case #'+ str(k+1) +': Volunteer cheated!')
    k=k+1
