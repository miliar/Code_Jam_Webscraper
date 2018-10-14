file = open("D-large (1).in","r")
outfile=open("outl2.txt","w")
t_case=int(file.readline())


def settler(naomi,ken):
    global a1, a2, d, fin, tmp, length, chk, out
    a1 = []
    a2 = []
    d = 0
    fin = 0
    while len(naomi) > 0:
        if naomi[0] < ken[0]:
            tmp = naomi.pop(0)
            a1.append(tmp)
            tmp = ken.pop()
            a2.append(tmp)
        else:
            length = len(ken) - 1
            while naomi[0] < ken[length]:
                length -= 1
            tmp = naomi.pop(0)
            a1.append(tmp)
            tmp = ken.pop(length)
            a2.append(tmp)
            d = d + 1
    a1.sort()
    a2.sort()
    while len(a1) > 0:
        chk = 0
        try:
            while a1[0] > a2[chk]:
                chk += 1
            a2.pop(chk)
            a1.pop(0)

        except:
            fin = len(a1)
            break
    out = "Case #" + str(k + 1) + ": " + str(d) + " " + str(fin)
    outfile.write(out + '\n')
    print(out)


for k in range(0,int(t_case)):
    count=file.readline()
    naomi=file.readline().strip().split()
    ken=file.readline().strip().split()
    for x in range(0,len(naomi)):
        naomi[x]=float(naomi[x])
    for x in range(0,len(ken)):
        ken[x]=float(ken[x])
    naomi.sort()
    ken.sort()
    settler(naomi,ken)
