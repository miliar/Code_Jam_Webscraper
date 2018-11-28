#!/usr/bin/python -u

def hitung(baris):
    addp = 0
    stdp = 0
    s = baris.strip().split()
    maxs = int(s[0])
    for i in range(maxs + 1):
        npeo = int(s[1][i])
        x = 0
        if stdp < i:
            x = i - stdp
            addp += x
        stdp += npeo + x
        #print i, npeo, stdp, addp
    return addp


# ---------------oOo``oOo-------
i = 0
nomor = 1
finput = open('input.txt', 'r')
for baris in finput:
    if i > 0:
        hasil = hitung(baris)
        output = 'Case #' + str(nomor) + ': ' + str(hasil)
        print output
        nomor += 1
    i += 1
