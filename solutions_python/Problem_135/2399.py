fr = open('een.in', 'r')
fw = open('een.out', 'w')

N = int(fr.readline())
for n in range(1, N+1):
    li = []

    for i in range(2):
        index = int(fr.readline())
        temp_li = []
        for j in range(4):
            temp_li.append(fr.readline().strip().split(' '))
        li.extend(temp_li[index-1])
    s = set([x for x in li if li.count(x) >= 2])
    out = ''
    if len(s) == 1:
        out = list(s)[0]
    elif len(s) > 1:
        out = 'Bad magician!'
    else:
        out = 'Volunteer cheated!'
    fw.write('Case #' + str(n) + ': ' + out + '\n')

fr.close()
fw.close()
