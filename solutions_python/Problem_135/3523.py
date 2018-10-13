fin = open('A.in','r')
fout = open('A.out','w')

case = int(fin.readline())

for i in range(case):
    ans1 = int(fin.readline())

    row1 = list()
    row2 = list()
    for p in range(4):
        line = fin.readline()

        if p == ans1 - 1:
            ddd = line.rstrip()
            row1 = ddd.split(' ')
    ans2 = int(fin.readline())
    for q in range(4):
        line = fin.readline()

        if q == ans2 - 1:
            ddd = line.rstrip()
            row2 = ddd.split(' ')

    inter = set(row1).intersection(set(row2))

    if(len(inter) == 1):
        fout.write('Case #{}: {}'.format(str(i+1),inter.pop()).rstrip())
        fout.write('\n')
    elif(len(inter) > 0):
        fout.write('Case #{}: Bad magician!\n'.format(i+1).rstrip())
        fout.write('\n')
    else:
        fout.write('Case #{}: Volunteer cheated!\n'.format(i+1).rstrip())
        fout.write('\n')

fin.close()
fout.close()