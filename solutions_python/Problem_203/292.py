fin=open('/home/dathuynh/Documents/Python/CodeJam/Testcase/A-large.in','r')
fout=open('/home/dathuynh/Documents/Python/CodeJam/Testcase/outputA.txt','w')

t = int(fin.readline())
for noCase in range(0,t):
    r,c = fin.readline().split()
    r = int(r)
    c = int(c)
    cake = []
    print '-'*10
    for j in range(r):
        row = fin.readline().rstrip()
        cake.append(list(row))
    for x in range(r):
        for y in range(c):
            if cake[x][y] != '?':
                i = 1
                while x - i >= 0 and cake[x-i][y] == '?':
                    cake[x-i][y] = cake[x][y]
                    i = i + 1

                i = 1
                if x + i < r and cake[x+i][y] == '?':
                    cake[x+i][y] = cake[x][y]
                    i = i + 1
    for x in range(r):
        for y in range(c):
            if cake[x][y] != '?':
                i = 1
                while y - i >= 0 and cake[x][y-i] == '?':
                    cake[x][y-i] = cake[x][y]
                    i = i + 1

                i = 1
                if y + i < c and cake[x][y+i] == '?':
                    cake[x][y+i] = cake[x][y]
                    i = i + 1
                # if y - 1 >= 0 and cake[x][y-1] == '?':
                #     cake[x][y-1] = cake[x][y]
                #
                # if y + 1 < c and cake[x][y+1] == '?':
                #     cake[x][y+1] = cake[x][y]
    fout.writelines('Case #{}:\n'.format(noCase+1))
    for x in range(r):
        for y in range(c):
            fout.write(cake[x][y])
        fout.write('\n')
    print cake
fout.close()
fin.close()
