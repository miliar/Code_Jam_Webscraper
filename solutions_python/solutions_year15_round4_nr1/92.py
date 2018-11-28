fin = open('A-large.in','r')
fout = open('output.txt','w')
t = int(fin.readline())
for count in range(1, t + 1):
    [r,c] = [int(i) for i in fin.readline().split()]
    room = [ "." for i in range(r)]
    label = [[0 for j in range(c)] for i in range(r)]
    for i in range(r):
        room[i] = fin.readline()
    for i in range(r):
        j = 0
        while (j < c) and (room[i][j] == '.'):
            j += 1;
        if (j < c):
            label[i][j] += 1;
        j = c - 1;
        while (j >= 0) and (room[i][j] == '.'):
            j -= 1;
        if (j >= 0):
            label[i][j] += 2;
    for j in range(c):
        i = 0
        while (i < r) and (room[i][j] == '.'):
            i += 1;
        if (i < r):
            label[i][j] += 4;
        i = r - 1;
        while (i >= 0) and (room[i][j] == '.'):
            i -= 1;
        if (i >= 0):
            label[i][j] += 8;
    #print(label)
    flag = 0;
    result = 0;
    for i in range(r):
        for j in range(c):
            if label[i][j] == 15:
                flag = 1;
            elif room[i][j] == '<' and (label[i][j] & 1):
                result += 1;
            elif room[i][j] == '>' and (label[i][j] & 2):
                result += 1;
            elif room[i][j] == '^' and (label[i][j] & 4):
                result += 1;
            elif room[i][j] == 'v' and (label[i][j] & 8):
                result += 1;
    fout.write('Case #'+str(count)+': ')
    if flag:
        fout.write('IMPOSSIBLE\n')
    else:
        fout.write(str(result) +'\n')
fin.close()
fout.close()
