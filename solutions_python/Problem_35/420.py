file = open('B-large.in')

lines = file.readlines()

file.close()
numcases = int(lines[0])
for i in range(len(lines)):
    lines[i] = lines[i].strip()
line=1
res = ""
for case in range(1,numcases+1):
    dimStr = lines[line].split(' ')
    h = int(dimStr[0])
    w = int(dimStr[1])
    
    line+=1
    m = []
    for i in range(h):
        row = lines[line].split(' ')
        row = map(int,row)
        m.append(row)
        line+=1

    count = -1
    basins={}
    

    file = open('out.txt','w')
    
    def getBasin(i,j):
        global count
        down = 0
        mini = 10,001
        direct = -1
        if i>0:
            if m[i-1][j] < mini:
                mini = m[i-1][j]
                direct = 0
        if j>0:
            if m[i][j-1] < mini:
                mini = m[i][j-1]
                direct = 1
        if j<w-1:
            if m[i][j+1] < mini:
                mini = m[i][j+1]
                direct = 2
        if i<h-1:
            if m[i+1][j] < mini:
                mini = m[i+1][j]
                direct = 3
        if m[i][j] <= mini:
            mini = m[i][j]
            direct = -1
            
        if direct == 0:
            return getBasin(i-1,j)
        if direct == 1:
            return getBasin(i,j-1)
        if direct == 2:
            return getBasin(i,j+1)
        if direct == 3:
            return getBasin(i+1,j)
        if direct == -1:
            if basins.has_key((i,j)):
                return basins[(i,j)]
            else:
                count+=1
                basins[(i,j)]=chr(97+count)
                return basins[(i,j)]

            return chr(97+count)

    res+="Case #"+str(case)+':\n'
    for i in range(h):
        for j in range(w):
            res+=getBasin(i,j)
            if j<w-1:
                res+=' '
        res+='\n'
        
file.writelines(res+'\n')


file.close()
