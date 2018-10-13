input = file("input.txt")
output = file("output.txt", "w")
result = []

temp = input.readline()
n=int(temp)

def getme(a, b, row, col):
    return a, b

def getleft(a, b, row, col):
    if b > 0 :
        return a, b-1
    else:
        return a, b

def getright(a, b, row, col):
    if b < col-1 :
        return a, b+1
    else:
        return a, b

def getup(a, b, row, col):
    if a > 0 :
        return a-1, b
    else:
        return a, b
    
def getdown(a, b, row, col):
    if a < row-1 :
        return a+1, b
    else:
        return a, b
    
calculate = [getme, getup, getleft, getright, getdown]
    
def getnext(a, b, dictionary, row, col):
    tt = []
    for i in calculate:
        o,p = i(a, b, row, col)
        tt.append(dictionary[o][p])
    
    cursor = 0
    min = tt[0]
    for i in range(5):
        if min > tt[i]:
            min = tt[i]
            cursor = i
    
    return calculate[cursor](a, b, row, col)
    
next = 0
prev = 1

for i in range(n):
    tag = ord('a')
    temp = input.readline().split()
    row, col = int(temp[0]), int(temp[1])
    
    graph = [ [0]*col for n in range(row)]
    result = [ [0]*col for n in range(row)]
    inter = [[[[], []] for m in range(col)] for n in range(row)]
    
    for m in range(row):
        temp = input.readline().split()
        for n in range(col):
            graph[m][n] = temp[n]
    
    for m in range(row):
        for n in range(col):
            o,p=getnext(m, n, graph, row, col)
            inter[m][n][next].append((o,p))
            inter[o][p][prev].append((m,n))     
    
    for m in range(row):
        for n in range(col):
            if result[m][n] != 0:
                continue
            stack = [(m,n)]
            tagch = chr(tag)
            tag+=1
            
            o,p = m,n
            while (o,p) != inter[o][p][next][0]:
                o,p = inter[o][p][next][0]
                stack.append((o,p))
            
            while len(stack)>0:
                o,p = stack.pop()
                result[o][p] = tagch
                for r,s in inter[o][p][prev]:
                    if result[r][s] == 0:
                        stack.append((r,s))
                        
    print >> output, "Case #%d:" % (i+1)
    for i in range(row):
        print >> output, " ".join(result[i])
            
            
            
input.close()
output.close()