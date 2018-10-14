fin = open('A-small-attempt0.in.txt','r')

fout = open('output.txt', 'w')

numCases = int(fin.readline())

for cases in range(numCases):
    rowin= [int(x) for x in fin.readline().split()]
    row = rowin[0]
    for i in range(4):
        if i == row-1 :
            lst1 = list(map(int,fin.readline().split()))
        else:
            dummy = list(map(int, fin.readline().split()))
    rowin= [int(x) for x in fin.readline().split()]
    row = rowin[0]
    for i in range(4):
        if i == row-1 :
            lst2 = list(map(int,fin.readline().split()))
        else:
            dummy = list(map(int, fin.readline().split()))

    count = 0
    item = 0
    for i in lst1:
        for j in lst2:
            if i == j:
                count = count+1
                item = i

    if count == 1:
        fout.write("Case #" + str(cases+1) + ": "+str(item)+'\n')
    elif count == 0:
        fout.write("Case #" + str(cases+1) + ": Volunteer cheated!"+'\n')
    else:
        fout.write("Case #" + str(cases+1) + ": Bad magician!"+'\n')

fin.close()
fout.close()