fin  = open('input.txt','r')
fout = open('output.txt','w')

cases = int(fin.readline())


for i in range(cases):
    guess1 = int(fin.readline())
    matrix1 = {}
    matrix1[1] = fin.readline().strip().split(' ')
    matrix1[2] = fin.readline().strip().split(' ')
    matrix1[3] = fin.readline().strip().split(' ')
    matrix1[4] = fin.readline().strip().split(' ')

    guess2 = int(fin.readline())
    matrix2 = {}
    matrix2[1] = fin.readline().strip().split(' ')
    matrix2[2] = fin.readline().strip().split(' ')
    matrix2[3] = fin.readline().strip().split(' ')
    matrix2[4] = fin.readline().strip().split(' ')

    a = set(matrix1[guess1]).intersection( set(matrix2[guess2]) )

    if(len(a) == 1):
        fout.write("Case #" + str(i + 1) + ": " + next(iter(a)) + "\n")
    elif(len(a) > 1):
        fout.write("Case #" + str(i + 1) + ": " + "Bad magician!" + "\n")
    elif(len(a) == 0):
        fout.write("Case #" + str(i + 1) + ": " + "Volunteer cheated!" + "\n")


