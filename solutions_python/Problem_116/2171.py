f =open("t.in","r")
f1 = open("b.out","w")
ct = int(f.readline().replace("\n",""))
data = []
i = 0

def checkRow(d):
    count  = 0
    draw = 0
    flag = 0
    dict = {'O':-1,'X':1,'T':0.5,'.':0}
    for p in d:
        count = 0
        for i in range(0,4):
            count = count + dict[p[i]]
            if count == -4 or count == -2.5:
                return [-1,flag]
            if count == 4 or count == 3.5:
                return [1,flag]
            if dict[p[i]] == 0:
                flag = -10
    return [0,flag]

def checkColumn(d):
    count  = 0
    draw = 0
    flag = 0
    dict = {'O':-1,'X':1,'T':0.5,'.':0}
    for i in range(0,4):
        count = 0        
        for p in d:
            count = count + dict[p[i]]
            if count == -4 or count == -2.5:
                return [-1,flag]
            if count == 4 or count == 3.5:
                return [1,flag]
    return [0,flag]


def checkDiagonal(d):
    count  = 0
    draw = 0
    flag = 0
    dict = {'O':-1,'X':1,'T':0.5,'.':0}
    for i in range(0,4):
        count = count + dict[d[i][i]]
        if count == -4 or count == -2.5:
            return [-1,flag]
        if count == 4 or count == 3.5:
            return [1,flag]
    count=0
    for i in range(0,4):
        count = count + dict[d[i][3-i]]
        if count == -4 or count == -2.5:
            return [-1,flag]
        if count == 4 or count == 3.5:
            return [1,flag]
    return [0,flag]      
        

for i in range(0,ct):
    data = []
    for j in range(0,4):
        data.append(f.readline().replace("\n",""))
    print(str(data))
    x = checkRow(data)
    y = checkColumn(data)
    z = checkDiagonal(data)
    print(str(x)+":"+str(y)+":"+str(z)+":")
    count = x[0]+y[0]+z[0]
    flag = x[1]+y[1]+z[1]
    if count < 0:
        f1.write("Case #"+str(i+1)+": O won\n")
    elif count > 0:
        f1.write("Case #"+str(i+1)+": X won\n")
    elif flag >= 0:
        f1.write("Case #"+str(i+1)+": Draw\n")
    elif flag < 0:
        f1.write("Case #"+str(i+1)+": Game has not completed\n")
    f.readline()
    
f1.close()
    
