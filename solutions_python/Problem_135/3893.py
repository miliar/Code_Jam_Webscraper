from array import*

f = open('A-small-attempt5.in', 'r')
g = open('A-small-attempt5output.txt', 'w')



case=int(f.readline())

for cases in range(case):
    p1 = int(f.readline()) -1
    g1 = []
    for j in range(4):
        g1.append([])
        for i in f.readline().split():
            g1[j].append(i)


    p2 = int(f.readline()) -1    
    g2 = []
    for j in range(4):
        g2.append([])
        for i in f.readline().split():
            g2[j].append(i)

    z = 0
    answer = [0]*4

    for i in range(4):
        for j in range(4):
            if g1[p1][j] == g2[p2][i]:
                answer[z] = g1[p1][j]
                z = z + 1
    

    if answer[1] > 0:
        g.write(str('Case #'+str(cases+1)+': Bad magician!\n'))
    elif answer[0] == 0:
        g.write(str('Case #'+str(cases+1)+': Volunteer cheated!\n'))
    else:
        g.write(str('Case #'+str(cases+1)+': '+ answer[0] + '\n'))
g.close()
f.close()
print('done')
