f = open("A-large.in")
all = f.readlines()

N = int(all.pop(0).strip())

for i in range(N):
    stevec = 0
    A, B = [int(j) for j in all.pop(0).strip().split(" ")]
    slovar = {}
    for j in range(A):
        line = all.pop(0).strip()
        line = line.split("/")[1:]
        tmp = ""
        for l in line:
            tmp += "/"+l
            slovar[tmp] = True
    # print slovar
    for j in range(B):
        add = all.pop(0).strip()
        line = add.split("/")[1:]
        tmp = ""
        for l in line:
            tmp += "/" + l
            try:
                if slovar[tmp]:
                    pass
            except:
                stevec += 1
                slovar[tmp] = True
    print "Case #"+str(i+1)+":", stevec
        
            