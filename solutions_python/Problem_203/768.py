"""
3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE
"""
def check_column(matrix,a,b,c,d,f):
    for x in range(a,b+1):
        for y in range(c,d+1):
            if matrix[x][y]!="?" and matrix[x][y]!=f:
                return False
    return True
def solution(matrix):
    label={}
    l1,l2=len(matrix),len(matrix[0])
    for i in range(l1):
        for j in range(l2):
            if matrix[i][j] not in label.keys():
                label[matrix[i][j]]=1
                x,y=[0,0],[0,0]
                while (i+x[0]-1>=0) and (j+y[0]-1>=0)and (check_column(matrix,i+x[0]-1,i+x[1],j+y[0]-1,j+y[1],matrix[i][j])):
                    x[0]-=1
                    y[0]-=1
                while (i+x[1]+1<l1) and (j+y[1]+1<l2) and (check_column(matrix, i+x[0], i+x[1]+1, j+y[0], j + y[1]+1,matrix[i][j])):
                    x[1] += 1
                    y[1] += 1
                while (i+x[0]-1>=0) and (check_column(matrix, i+x[0]-1, i+x[1], j+y[0], j + y[1],matrix[i][j])):
                    x[0]-=1
                while (i+x[1]+1<l1) and (check_column(matrix, i+x[0], i+x[1]+1, j+y[0], j + y[1],matrix[i][j])):
                    x[1]+=1
                while (j+y[0]-1>=0) and (check_column(matrix,i+x[0],i+x[1],j+y[0]-1,j+y[1],matrix[i][j])):
                    y[0]-=1
                while (j+y[1]+1<l2) and check_column(matrix,i+x[0],i+x[1],j+y[0],j+y[1]+1,matrix[i][j]):
                    y[1]+=1
                for a in range(i+x[0],i+x[1]+1):
                    for b in range(j+y[0],j+y[1]+1):
                        matrix[a][b]=matrix[i][j]
    return matrix
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]
    temp =[]
    for j in range(n):
        x=input()
        temp.append(list(x))
    result=solution(temp)
    print("Case #{}:".format(i))
    for index,i in enumerate(result):
        for index2,j in enumerate(i):
            print(j,end="")
        print()
