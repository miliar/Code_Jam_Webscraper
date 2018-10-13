fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
N = fin.readline()

n = int(N)

for i in range(0,n):
    numBlocks = int(fin.readline())
    Na = []
    for j in (fin.readline()).split():
        Na.append(float(j))
    Ke = []
    for j in (fin.readline()).split():
        Ke.append(float(j))

    Na2 = list(Na)
    Ke2 = list(Ke)
    
    nPts1 = 0
    nPts2 = 0
    ########################################################
    for j in range(0,numBlocks):
        tempNa = min(Na)
        tempKe = 0
        if tempNa > max(Ke):
            tempKe = min(Ke)
            nPts1 += 1
            Na.remove(tempNa)
            Ke.remove(tempKe)
            continue
        else:
            temp = []
            for k in Ke:
                if k > tempNa:
                    temp.append(k)
            tempKe = min(temp)
            Ke.remove(tempKe)
            Na.remove(tempNa)
            continue
    #########################################################
    
    for j in range(0,numBlocks):
        tempNa = min(Na2)
        minKe = min(Ke2)
        tempKe = 0
        if tempNa < minKe:
            tempKe = max(Ke2)
            Ke2.remove(tempKe)
            Na2.remove(tempNa)
            continue
        else:
            tempKe = min(Ke2)
            nPts2 += 1
            Ke2.remove(tempKe)
            Na2.remove(tempNa)
            continue
        

    s = 'Case #'
    s+= str(i+1)
    s+= ': '
    s+= "%d %d" % (nPts2, nPts1)
    s+= '\n'
    fout.write(s)

fin.close()
fout.close()
