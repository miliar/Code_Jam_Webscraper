import sys

def hitung(d1, d2):
    angka = ''
    ada = 0
    aa1 = d1.split()
    aa2 = d2.split()
    for a in aa1:
        if a in aa2:
            angka = a
            ada += 1
    if ada == 1:
        hasil = angka
    elif ada == 0:
        hasil = 'Volunteer cheated!'
    elif ada > 1:
        hasil = 'Bad magician!'
    return hasil


i = 0
nomor = 1
p1 = -1
p2 = -1
for baris in sys.stdin:
    data = baris.strip()
    if i == 0:
        n = int(data)
    elif i == 1:
        p1 = int(data) + 1
    elif i == p1:
        d1 = data
    elif i == 6:
        p2 = int(data) + 6
    elif i == p2:
        d2 = data
    if i == 10:
        jawab = hitung(d1, d2)
        print 'Case #' + str(nomor) + ': ' + jawab
        i = 0
        nomor += 1
    i += 1
