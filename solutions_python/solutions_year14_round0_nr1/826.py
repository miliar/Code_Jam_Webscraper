fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
N = fin.readline()

n = int(N)

for i in range(0,n):
    firstRow = int(fin.readline())-1
    firstTable = [0,0,0,0]
    for j in range(0,4):
        temp = []
        for k in (fin.readline()).split():
            temp.append(int(k))
        firstTable[j] = temp
    
    secondRow = int(fin.readline())-1
    secondTable = [0,0,0,0]
    for j in range(0,4):
        temp = []
        for k in (fin.readline()).split():
            temp.append(int(k))
        secondTable[j] = temp

    s = 'Case #'
    s+= str(i+1)
    s+= ': '

    values = []
    for j in firstTable[firstRow]:
        print j
        if j in secondTable[secondRow]:
            values.append(j)

    if len(values) == 0:
        s+= 'Volunteer cheated!'
    elif len(values) == 1:
        s+= str(values[0])
    else:
        s+= 'Bad magician!'

    s+= '\n'
    fout.write(s)

fin.close()
fout.close()
