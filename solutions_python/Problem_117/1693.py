def lawnmower(r, c, grass):
    lst = []
    for i in range(r):
        lst.append(max(grass[i]))
    m = max(lst)
    start = []
    column = columns(r, c, grass)
    for i in range(r):
        start.append([m]*c)
    if start == grass:
        return "YES"
    for i in range(r):
        for j in range(c):
            if start[i][j] > grass[i][j]:
                if grass[i][j] == max(grass[i]):
                    #print(i, j)
                    for k in range(c):
                        start[i][k] = grass[i][j]
                        #print("X",start)
                if grass[i][j] == max(column[j]):
                    #print(i, j)
                    for k in range(r):
                        start[k][j] = grass[i][j]
                        #print("Y",start)
                #print("start",start)
                if start == grass:
                    return "YES"
    #print(start, grass)
    return "NO"


def columns(r, c, matrix):
    lst = []
    for i in range(c):
        l = []
        for j in range(r):
            l.append(matrix[j][i])
        lst.append(l)
    #print("lst", lst)
    return lst
    
f = open('B-small-attempt1.in','r')
output = open('lawnmower.txt','w')
lines = f.readline()
for i in range(int(lines)):
    lst = [int(x) for x in f.readline().split()]
    grass = []
    for j in range(lst[0]):
        grass.append([int(x) for x in f.readline().split()])
    #print(lst[0], lst[1], grass)
    result = lawnmower(lst[0], lst[1], grass)
    output.write('Case #{0}: {1}\n'.format(i+1, result))
f.close()
output.close()
                
    
    
