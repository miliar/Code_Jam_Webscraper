import sys
sys.path.append('/users/ahn/desktop/codejam/round 1C')

file = open('/users/ahn/desktop/codejam/round 1C/input.txt')

T = int(file.readline())

R = []
C = []
tile = []
possibility = []
for i in range(0,T):
    tile += [[]]
    possibility += [True]

for i in range(0,T):
    temp = file.readline().split(' ')
    R += [int(temp[0])]
    C += [int(temp[1])]
    for j in range(0,R[i]):
        tile[i] += [[]]
        temp = file.readline()
        for k in range(0,C[i]):
            if temp[k] == '.':
                tile[i][j] += [0]
            else:
                tile[i][j] += [1]
                
file.close()

for i in range(0,T):
    for j in range(0,R[i]):
        if_break = False
        for k in range(0,C[i]):
            if tile[i][j][k] == 1:
                if j+1 == R[i] or k+1 == C[i]:
                    if_break = True
                    possibility[i] = False
                    break
                elif tile [i][j][k+1] != 1 or tile[i][j+1][k] != 1 or tile[i][j+1][k+1] != 1:
                    if_break = True
                    possibility[i] = False
                    break
                else:
                    tile[i][j][k] = 2
                    tile[i][j+1][k+1] = 2
                    tile[i][j+1][k] = 3
                    tile[i][j][k+1] = 3
        if if_break:
            break
    for j in range(0,R[i]):
        for k in range(0,C[i]):
            if tile[i][j][k] == 0:
                tile[i][j][k] = '.'
            elif tile[i][j][k] == 1:
                tile[i][j][k] = '#'
            elif tile[i][j][k] == 2:
                tile[i][j][k] = '/'
            else:
                tile[i][j][k] = '\\'





output=''

for i in range(0,T):
    output += 'Case #'+str(i+1)+':\n'
    if not possibility[i]:
        output += 'Impossible\n'
    else:
        for j in range(0,R[i]):
            for k in range(0,C[i]):
                output += tile[i][j][k]
            output += '\n'



file = open('/users/ahn/desktop/codejam/round 1C/output.txt','w')
file.write(output)
file.close()