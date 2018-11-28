fin = open('B-large.in','r')
fout = open('output.txt','w')
t = int(fin.readline())
for count in range(1, t + 1):
    line = fin.readline().strip()
    n = list(line)
    n = list(map(int, n));
    for i in range(1, len(n)):
        if n[i] < n[i - 1]:
            j = i - 1;
            while (j > 0) and (n[j] == n[j - 1]):
                j = j - 1;
            n[j] = n[j] - 1;
            for k in range(j + 1, len(n)):
                n[k] = 9;
            break;
    fout.write('Case #' + str(count) + ': ')
    if n[0] != 0:
        fout.write(str(n[0]))
    for i in range(1, len(n)):
        fout.write(str(n[i]))
    fout.write('\n')
fin.close()
fout.close()
