fin = open("A-small-attempt0.in", 'r')
fout= open("out.txt", 'w')


def sign(lis):
    l = [0]
    for i in range(len(lis)):
        if l[-1] != lis[i]:
            l.append(lis[i])
    return l

count = 0
dictd = dict()
fiList = []
testCaNum= int(fin.readline().strip())
for testCa in range(1, testCaNum +1):
    count = 0
    fiList = []
    nm = []
    fch = int(fin.readline().strip())
    for num in range(0,fch):
        fiList.append(list(fin.readline().strip()))
        nm.append(0)
    fegla = False
    for num in range(0,fch-1):
        if ( sign(fiList[num]) != sign(fiList[num+1])):
            fegla = True
            break
    fl = True
    c = 0
    hl = sign(fiList[0])
    if not fegla:    
        for le in range(len(hl)):
            c = 0
            for num in range(0,fch):
                nm[num]=0
                while (True):
                    if(len(fiList[num]) == 0):
                        break
                    if fiList[num][0] == hl[le]:
                        fiList[num].pop(0)
                        c = c + 1
                        nm[num] = nm[num] + 1
                    else:
                        break
            c = c/fch    
            if (c > int(c) + 0.5):
                c = int(c) + 1
            else:
                c = int(c)
            for num in range(0,fch):
                count = count + abs(c - nm[num])
    
    fout.write("Case #"+str(testCa)+": ")
    if(fegla == True):
        fout.write("Fegla Won\n")
    else:
        fout.write(str(count)+"\n")
        
fin.close()
fout.close()
