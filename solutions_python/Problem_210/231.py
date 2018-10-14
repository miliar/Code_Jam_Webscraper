filename = "C:\\Users\\Andri_000\\Downloads\\python\\codejam2017\\Round 1C\\B\\B-small-attempt1"

fin = open(filename+".in")
fout = open(filename+".out","w")
trials = int(fin.readline())

       
for T in xrange(trials):
    
    ac, aj = map(int, fin.readline().split(' '))
    cdjk = []
    cdlen, jklen = 0, 0
    for i in range(ac):
        x, y = map(int, fin.readline().split(' '))
        cdjk.append((x, y, 0))
        cdlen += 1
    for i in range(aj):
        x, y = map(int, fin.readline().split(' '))
        cdjk.append((x, y, 1))
        jklen += 1
    
    zt = min(map(lambda x: x[0], cdjk))
    cdjk = sorted(map(lambda x: (x[0]-zt, x[1]-zt, x[2]), cdjk))
    cdjk.append((1440,1440,cdjk[0][2]))
    
    merges, tot = [], {0:0, 1:0}
    for i in range(len(cdjk)-1):
        if cdjk[i][2] == cdjk[i+1][2]:
            merges.append((cdjk[i+1][0]-cdjk[i][1], cdjk[i][2]))
    for el in cdjk:
        tot[el[2]] += el[1]-el[0]
    merges = sorted(merges)
    
    ans = 0
    for i in range(len(cdjk)-1):
        if cdjk[i][2] == cdjk[i+1][2]:
            ans += 2
        else:
            ans += 1
    
    
    #print ans
    
    for el in merges:
        if tot[el[1]] + el[0] <= 720 and 1440-tot[1-el[1]] - el[0] >= 720:
            tot[el[1]] += el[0]
            #tot[1-el[1]] += el[0]
            ans -= 2

    #print cdjk, merges, tot

    

    fout.write("Case #{0}: {1}\n".format(T+1, ans))
    print "Case #{0} done".format(T+1)
                    
fin.close()
fout.close()