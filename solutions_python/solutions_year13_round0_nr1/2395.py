f = open('i2.in','r')
f2 = open('o2.txt','w')
n = f.readline()
for i in range(1, int(n)+1):
    flag = False
    matrix = []
    row = []
    for m in range(0, 4):
        txt = f.readline()
        row = list(txt)
        matrix.append(row)
    f.readline()
    for x in range(0, 4):
        for y in range(0, 4):
            el = matrix[x][0]
            if(el == 'T'):
                el = matrix[x][1]
            if((el != matrix[x][y] and matrix[x][y] != 'T') or el == '.'):
                y = 0
                break
        if(y == 3):
            result = 'Case #'+str(i)+': '+ el + ' won'
            flag = True
            break
    if(flag == False):
        for x in range(0, 4):
            for y in range(0, 4):
                el = matrix[0][x]
                if(el == 'T'):
                    el = matrix[1][x]
                if((el != matrix[y][x] and matrix[y][x] != 'T') or el == '.'):
                    y = 0
                    break
            if(y == 3):
                result = 'Case #'+str(i)+': '+ el + ' won'
                flag = True
                break
    if(flag == False):
        for x in range(0, 4):
            el = matrix[0][0]
            if(el == 'T'):
                el = matrix[1][1]
            if((el != matrix[x][x] and matrix[x][x] != 'T') or el == '.'):
                x = 0
                break
        if(x == 3):
            result = 'Case #'+str(i)+': '+ el + ' won'
            flag = True
            
    if(flag == False):
        for x in range(0, 4):
            el = matrix[3][0]
            if(el == 'T'):
                el = matrix[2][1]
            if((el != matrix[3-x][x] and matrix[3-x][x] != 'T') or el == '.'):
                x = 0
                break
        if(x == 3):
            result = 'Case #'+str(i)+': '+ el + ' won'
            flag = True
            
    if(flag == False):
        for x in range(0, 4):
            for y in range(0, 4):
                if(matrix[x][y] == '.'):
                    result = 'Case #'+str(i)+': '+'Game has not completed'
                    flag = True
                    break
            if(flag == True):
                break
    if(flag == False):
        result = 'Case #'+str(i)+': '+'Draw'
    print result
    f2.write(result+'\n')
f.close()
f2.close()
