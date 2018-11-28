import copy, itertools
with open("B-large.in") as f:
    n = int(f.readline())
    for i in range(n):
        y,x = [int(a) for a in f.readline().strip().split()]
        if x==1 and y==1:
            neverused = f.readline()
            print("Case #",i+1,":",sep='') # print the fucker
            print('a')
            continue
        field = []
        for j in range(y):#build field
            field.append([int(a) for a in f.readline().strip().split()])
        cfield = copy.deepcopy(field)#write flow direction in a copy
        for s in range(x):
            for a in range(y):
                checks = []
                if not a == 0: checks.append((field[a-1][s],"n"))
                if not s == 0: checks.append((field[a][s-1],"w"))
                if not s == x-1: checks.append((field[a][s+1],"e"))
                if not a == y-1: checks.append((field[a+1][s],"s"))
                #print(checks)
                m = min(checks,key=lambda x:x[0])
                if m[0] < field[a][s]:
                    cfield[a][s] = m[1]
                else:
                    cfield[a][s] = "b"
        cou = itertools.count() #number the basins
        for a in range(y):
            for s in range(x):
                if cfield[a][s]=="b":
                    cfield[a][s] = cou.__next__()
        #print(cfield)
        for a in range(y):#number the rest of the field
            atmp = a
            for s in range(x):
                a = atmp
                if isinstance(cfield[a][s],int): continue
                else:
                    lis = [(a,s)]
                    while not isinstance(cfield[a][s],int):

                        if cfield[a][s] == "n":
                            assert a!= 0
                            a -= 1
                        elif cfield[a][s] == "w":
                            assert s!=0
                            s -= 1
                        elif cfield[a][s] == "e":
                            s += 1
                        elif cfield[a][s] == "s":
                            a += 1
                        lis.append((a,s))
                    b = cfield[a][s]
                    for p in lis:
                        cfield[p[0]][p[1]] = b
        d = {}#numbers to letters
        cou = itertools.count(97)
        for line in cfield:
            for entry in line:
                if entry not in d:
                    d[entry] = chr(cou.__next__())
                entry = d[entry]
        print("Case #",i+1,":",sep='') # print the fucker
        #print (cfield)
        for line in cfield:
            s = ""
            for entry in line:
                s += d[entry]
                s += " "
            s = s[:-1]
            print(s)

