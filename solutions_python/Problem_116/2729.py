def checkrows(matrix,size):
    for col in range(size):
        X = 0
        O = 0
        for values in matrix.values():
            if 'X' in values[col]:
                X += 1
            elif 'O' in values[col]:
                O += 1
            elif 'T' in values[col]:
                X += 1
                O += 1
        if (X>=4):
            return 'X'
        elif (O>=4):
            return 'O'
    return 'N'

def checkcol(matrix,size):
    for i in range(size):
        X = 0
        O = 0
        for j in range(size):
            if 'X' in matrix[i][j]:
                X += 1
            elif 'O' in matrix[i][j]:
                O += 1
            elif 'T' in matrix[i][j]:
                X += 1
                O += 1
            if (X>=4):
                return 'X'
            elif (O>=4):
                return 'O'
    return 'N'

def checkdiagleft(matrix,size):
    if size <4:
        return 'N'
    else:
        start = size-3
        for i in range(start,0,-1):
            a = i-1
            b = 0
            X = 0
            O = 0
            for j in range(a,size):
                if matrix[j][b] == 'X':
                    X += 1
                elif matrix[j][b] == 'O':
                    O += 1
                elif matrix[j][b] == 'T':
                    X += 1
                    O += 1
                if X == 4:
                    return 'X'
                    break
                elif O == 4:
                    return 'O'
                    break
                b+=1
        for i in range(0,start):
            X = 0
            O = 0
            b = 0
            for j in range(i,size):
                if matrix[j][b] == 'X':
                    X+=1
                elif matrix[j][b] == 'O':
                    O+=1
                elif matrix[j][b] == 'T':
                    X+=1
                    O+=1
                if X==4:
                    return 'X'
                    break
                elif O==4:
                    return 'O'
                    break
                b+=1
        return 'N'

def checkdiagright(matrix,size):
    if size<4:
        return 'N'
    else:
        start = 3
        end = size-3
        for i in range(start,size):
            X = 0
            O = 0
            b = 0
            for j in range(i,-1,-1):
                if matrix[j][b] == 'X':
                    X+=1
                elif matrix[j][b] == 'O':
                    O+=1
                elif matrix[j][b] == 'T':
                    X+=1
                    O+=1
                if X==4:
                    return 'X'
                    break
                elif O==4:
                    return 'O'
                    break
                b+=1
            if (X==4) or (O==4):
                break
        if (X<4) and (O<4):
            for i in range(end,0,-1):
                a = i-1
                X = 0
                O = 0
                b = size-1
                for j in range(a,size):
                    if matrix[j][b] == 'X':
                        X += 1
                    elif matrix[j][b] == 'O':
                        O += 1
                    elif matrix[j][b] == 'T':
                        X += 1
                        O += 1
                    if X==4:
                        return 'X'
                        break
                    elif O==4:
                        return 'O'
                        break
                    b-=1
                if (X==4) or (O==4):
                    break
    if (X<4) and (O<4):
        return 'N'

inFile = open('A-small-attempt3.in','r')
outFile = open('codejam1.txt','w')
filesize = int(inFile.readline())

temp = inFile.readline()

lines = []
for i in temp:
    i = i.strip('\n')
    if i != '':
        lines.append(i)

size = len(lines)
matrix = {}
matrix[0] = lines
output = ''
for a in range(filesize):
    if a==0:
        for b in range(size-1):
            temp = inFile.readline()
            lines = []
            for i in temp:
                i = i.strip('\n')
                if i != '':
                    lines.append(i)
            matrix[b+1] = lines
    else:
        for b in range(size):
            temp = inFile.readline()
            lines = []
            for i in temp:
                i = i.strip('\n')
                if i != '':
                    lines.append(i)
            matrix[b] = lines
    temp = inFile.readline()
    check = checkrows(matrix,size)
    if check != 'N':
        output = 'Case #'+str(a+1)+': '+check+' won'+'\n'
        print 'Case #'+str(a+1)+':',check,'won'
    else:
        check2 = checkcol(matrix,size)
        if check2 != 'N':
            output = 'Case #'+str(a+1)+': '+check2+' won'+'\n'
            print 'Case #'+str(a+1)+':',check2,'won'
        else:
            check3 = checkdiagleft(matrix,size)
            if check3 != 'N':
                output = 'Case #'+str(a+1)+': '+check3+' won'+'\n'
                'Case #'+str(a+1)+': '+check3+' won'+'\n'
                print 'Case #'+str(a+1)+':',check3,'won'
            else:
                check4 = checkdiagright(matrix,size)
                if check4 != 'N':
                    output = 'Case #'+str(a+1)+': '+check4+' won'+'\n'
                    print 'Case #'+str(a+1)+':',check4,'won'
                else:
                    end = 'N'
                    for c in matrix.values():
                        if '.' in c:
                            output = 'Case #'+str(a+1)+': Game has not completed'+'\n'
                            print 'Case #'+str(a+1)+': Game has not completed'
                            break
                        else:
                            end = 'Y'
                    if end == 'Y':
                        output = 'Case #'+str(a+1)+': Draw'+'\n'
                        print 'Case #'+str(a+1)+': Draw'
                    
    outFile.write(str(output))
outFile.close()
