fin = open('C-large.in','r')
fout = open('output.txt','w')
t = int(fin.readline())
for count in range(1, t + 1):
    line = fin.readline().strip()
    n = int(line.split()[0])
    k = int(line.split()[1])
    floor = 2 ** (k.bit_length() - 1) - 1;
    minfloor = (n - floor) // (floor + 1);
    num = (n - floor) % (floor + 1);
    if (k - floor <= num):
        distance = minfloor;
    else:
        distance = minfloor - 1;
        
    fout.write('Case #' + str(count) + ': ')
    if (distance % 2 == 0):
        fout.write(str(distance // 2) + ' ' + str(distance // 2))
    else:
        fout.write(str(distance // 2 + 1) + ' ' + str(distance // 2))
    fout.write('\n')
fin.close()
fout.close()
