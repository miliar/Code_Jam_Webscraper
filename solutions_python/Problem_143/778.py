def dec_to_bin(x):
    return bin(x)[2:]

def insertZero(x,size):
    for i in range(len(x),size):
        x = '0' + x
    return x

def createTable(x,y):
    t = []
    for i in range(x):
        t.append([0]*y)
        
    for i in range(0,x):
        for j in range(0,y):
            t[i][j] = int(bin(i&j),2)
    return t


infile = open("B-small-attempt0.in","r")
y = infile.readline()
y = y.split()
N  = int(y[0])

and_table = createTable(1001,1001)
for i in range(0,N):
    count = 0
    y = infile.readline()
    y = y.split()
    a = int(y[0])
    b = int(y[1])
    k = int(y[2])

    for c in range(a):
        for d in range(b):
            if and_table[c][d] < k :
                count += 1

    s = "Case #" + str(i+1) + ":"
    print s,count
    
