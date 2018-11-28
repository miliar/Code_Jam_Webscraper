fin = file('in.txt','r')
fout = file('out.txt','w')

n = int(fin.readline())

for i in range(n):
    row1 = int(fin.readline())
    cards1 = []
    for j in range(4):
        cards1.append(map(int, fin.readline().split()))

    row2 = int(fin.readline())
    cards2 = []

    for j in range(4):
        cards2.append(map(int, fin.readline().split()))

    result = list(set(cards1[row1-1]) & set(cards2[row2-1]))
    if len(result) == 1:
        fout.write("Case #%d: %d\n"%(i+1,result[0]))
    elif len(result) == 0:
        fout.write("Case #%d: Volunteer cheated!\n"%(i+1))
    else:
        fout.write("Case #%d: Bad magician!\n"%(i+1))

fout.close()
fin.close()
