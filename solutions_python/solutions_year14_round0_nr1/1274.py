__author__ = 'lexplua'
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
n_cases = int(fin.readline().strip())
for i in range(n_cases):
    ans1 = int(fin.readline().strip())-1
    row = []
    for r in range(4):
        row.append([int(x) for x in fin.readline().strip().split()])
    pur = set(row[ans1])
    ans2 = int(fin.readline().strip())-1
    row = []
    for r in range(4):
        row.append([int(x) for x in fin.readline().strip().split()])
    pur.intersection_update(set(row[ans2]))
    fout.write("Case #{}: ".format(i+1))
    if len(pur) == 1:
        fout.write("{}".format(list(pur)[0]))
    elif len(pur) == 0:
        fout.write('Volunteer cheated!')
    else:
        fout.write('Bad magician!')
    fout.write('\n')
fin.close()
fout.close()