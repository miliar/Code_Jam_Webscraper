infile = open("infile.txt","r")
inlist = infile.readlines()
outfile = open("out.txt","w")
cases = eval(inlist.pop(0))

for i in range(len(inlist)): inlist[i] = inlist[i].strip("\n")

table = []
i = 0
while i < len(inlist):
    N = eval(inlist[i].split()[0])
    table.append(inlist[i:i+N+1])
    i+=N+1

for i in table:
    for j in range(len(i)):
        i[j] = [eval(val) for val in i[j].split()]

for case in range(len(table)):
    set = table[case]
    done = False
    [y,x] = set[0]
    m = False
    for i in range(1,y+1):
        for j in range(x):
            if not m: m = set[i][j]
            elif set[i][j]<m: m = set[i][j]

    for i in range(1,y+1):
        for j in range(x):
            if not done:
                if set[i][j] == m:
                    c1 = True
                    c2 = True
                    for a in range(1,y+1):
                        if set[a][j] != m:
                            c1 = False
                            break
                    for b in range(0,x):
                        if set[i][b] != m:
                            c2 = False
                            break

                    if not c1 and not c2:
                        print("Case #"+str(case+1)+": "+"NO", file=outfile)
                        done = True
                        break

    if not done:
        print("Case #"+str(case+1)+": "+"YES", file=outfile)

outfile.close()
infile.close()