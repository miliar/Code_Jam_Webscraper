fin = open("inputA_S.txt", 'r')
fout = open("outputA_S.txt", 'w')
t = int(fin.readline())
for test in range(t):
    s_max , line = fin.readline().split()
    s = 0
    clapping = 0
    for i in range(len(line)):
        if clapping >= i:
            clapping += int(line[i])
        else:
            if line[i] != 0:
                s += i - clapping
                clapping = i + int(line[i])
    fout.write("Case #" + str(test + 1) + ': ' + str(s) + '\n')
fin.close()
fout.close()
