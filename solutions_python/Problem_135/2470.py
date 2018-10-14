f = open('A-small-attempt0.in')
# f = open('test.in')
count = int(f.readline())
output = ''
a1 = [[]] * 4
a2 = [[]] * 4
for x in range(1,count + 1):
    ans1 = int(f.readline()) - 1
    a1[0] = f.readline()
    a1[1] = f.readline()
    a1[2] = f.readline()
    a1[3] = f.readline()

    ans2 = int(f.readline()) - 1
    a2[0] = f.readline()
    a2[1] = f.readline()
    a2[2] = f.readline()
    a2[3] = f.readline()

    t1 = a1[ans1].split()
    t2 = a2[ans2].split()

    cardsCount = 0
    t = 0
    for y in range(0,4):
        try:
            t2.index(t1[y])
            t = t1[y]
            cardsCount += 1
        except:
            continue

    if cardsCount == 1:
        output += 'Case #' + str(x) + ': ' + t + '\n'
    elif cardsCount > 1:
        output += 'Case #' + str(x) + ': Bad magician!\n'
    elif cardsCount == 0:
        output += 'Case #' + str(x) + ': Volunteer cheated!\n'


print(output)
newf = open('output.txt','w')
newf.write(output)
