fin = 'A-large.in'
fout = 'A-large.out'

def ova(fin, fout):
    fin = open(fin)
    fout = open(fout, 'w')

    t = int(fin.readline()[:-1])
    print(t)
    for i in range(1, t+1):
        s = fin.readline()[:-1].split(' ')
        m, shy = int(s[0]), s[1]
        d = 0
        need = 0
        for j in range(0, m+1):
            d = d + 1 - int(shy[j])
            if d > need:
                need = d
        
        fout.write("Case #{0}: {1}\n".format(i, need))
    fin.close()
    fout.close()

ova(fin, fout)
