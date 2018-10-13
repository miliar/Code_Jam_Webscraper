fin = open('A-large.in', 'r')
fout = open('output.txt', 'w')
T = int(fin.readline())
for cID in range(T):
    print('case: {}'.format(cID))
    Rstr, Cstr = fin.readline().strip().split()
    R = int(Rstr)
    C = int(Cstr)
    cake = []
    for i in range(R):
        cake.append(list(fin.readline().strip()))
    flag = False
    s = -1
    for i in range(R):
        if cake[i].count('?') == len(cake[i]):
            if i == 0:
                flag = True
            else:
                for j in range(C):
                    cake[i][j] = cake[i-1][j]
        else:
            j = 0
            while cake[i][j] == '?':
                j += 1
            while j > 0:
                cake[i][j-1] = cake[i][j]
                j = j-1
            for j in range(C):
                if cake[i][j] == '?':
                    cake[i][j] = cake[i][j-1]
    if flag:
        i = 0
        while '?' in cake[i]:
            i += 1
        for j in range(i):
            for c in range(C):
                cake[j][c] = cake[i][c]
    fout.write("Case #{}:\n".format(cID+1))
    for line in cake:
        for c in line:
            fout.write(c)
        fout.write('\n')