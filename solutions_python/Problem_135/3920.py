file = open("A-small-attempt2.in-2.txt", mode = 'r')
outfile = open('output.out', mode = 'w')
x = int(file.readline()[:-1])

result = []
for k in range(x):
    row1 = int(file.readline()[:-1])
    for i in range (4):
        if i+1 == row1:
            r1 = file.readline()[:-1].split(' ')
        else:
            n = file.readline()[:-1]
    row2 = int(file.readline()[:-1])
    for i in range(4):
        if i+1 == row2:
            r2 = file.readline()[:-1].split(' ')
        else:
            n = file.readline()[:-1]
    answer = -1
    for i in range(4):
        if r1[i] in r2:
            if answer == -1:
                answer = r1[i]
            else:
                answer = 0
    result.append(answer)

for k in range(x):
    if result[k] == 0:
#        print('Case #'+str(k+1)+': Bad magician!')
        outfile.write('Case #'+str(k+1)+': Bad magician!\n')
    elif result[k] == -1:
#       print('Case #'+str(k+1)+': Volunteer cheated!')
        outfile.write('Case #'+str(k+1)+': Volunteer cheated!\n')
    else:
#        print('Case #'+str(k+1)+': '+result[k])
        outfile.write('Case #'+str(k+1)+': '+result[k]+'\n')

file.close()
outfile.close()

