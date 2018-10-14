import os
   
def analyse (lawn, n, m):
    
    for i in range(n):
        for j in range (m):
            if lookH (lawn, i,j, n, m) and lookV(lawn,i,j, n, m):
                return("NO")
    return ("YES")

def lookH(lawn, i, j, n, m):
    startval = lawn[i][j]
    result = False
    for a in range (n):
        if lawn [a][j] > startval:
            result = True
    return(result)
            
def lookV (lawn, i, j, n, m):
    startval = lawn[i][j]
    result = False
    for a in range (m):
        if lawn [i][a] > startval:
            result = True
    return (result)

    
    
filein = open ('B-small-attempt1.in', 'r') 
outfile = open ('sample.out', 'wt')
instances = int(filein.readline())

for i in range (instances):
    l = filein.readline()
    n,m = l.split()
    n = int(n)
    m = int(m)
    lawn = []
    for rows in range (n):
        row = list(filein.readline())
        while row.count(' ')>0:
            row.remove(' ')
        while row.count('\n')>0:
            row.remove('\n')
        lawn.append(row)
    print (lawn)
    stringStart = str('Case #' + str(i+1) + ': ')
    answer = analyse(lawn, n, m)
    print(stringStart + answer)
    outfile.write(stringStart + answer)
    outfile.write('\n')
filein.close()
outfile.close()
