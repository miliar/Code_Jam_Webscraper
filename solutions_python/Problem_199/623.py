fin = open('A-large.in','r')
fout = open('output.txt','w')
t = int(fin.readline())
for count in range(1, t + 1):
    line = fin.readline()
    s = list(line.split()[0])
    k = int(line.split()[1])
    result = 0;
    for i in range(len(s) - k + 1):
        if (s[i] == '-'):
            result = result + 1
            for j in range(i + 1, i + k):
                if (s[j] == '-'):
                    s[j] = '+'
                elif (s[j] == '+'):
                    s[j] = '-'
    rest = 0;
    for i in range(len(s) - k + 1, len(s)):
        if (s[i] == '-'):
            rest = rest + 1
    fout.write('Case #' + str(count) + ': ')
    if rest == 0:
        fout.write(str(result))
    else:
        fout.write('IMPOSSIBLE')
    fout.write('\n')
fin.close()
fout.close()
