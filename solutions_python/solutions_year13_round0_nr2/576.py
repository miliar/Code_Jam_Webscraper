def check(matrix, N, M):
    new_matrix = []
    max_ = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem > max_:
                max_ = elem

    for row in range(N):
        line = []
        for col in range(M):
            line.append(max_)
        new_matrix.append(line)

    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if elem < new_matrix[i][j]:
                row_can_be_changed = True
                col_can_be_changed = True

                #check row
                for x in matrix[i]:
                    if x > elem:
                        row_can_be_changed = False
                #check column
                for x in matrix:
                    if x[j] > elem:
                        col_can_be_changed = False

                if row_can_be_changed:
                    for x in range(M):
                        new_matrix[i][x] = elem
                elif col_can_be_changed:
                    for x in range(N):
                        new_matrix[x][j] = elem
                else:
                    return False
    return True
    

f = open('B-large.in', 'r')

output = open('output.txt','w')

T = int(f.readline())

for i in range(1,T+1):
    matrix = []

    line1 = (f.readline().rstrip()).split(' ')

    N = int(line1[0])
    M = int(line1[1])

    for j in range(N):
        matrix.append([int(x) for x in (f.readline().rstrip()).split(' ')])

    if check(matrix,N,M):
        result = "YES"
    else:
        result = "NO"

    text = 'Case #'+str(i)+': '+ str(result)

    print(text,file=output)
    #print(text)

f.close()
output.close()
