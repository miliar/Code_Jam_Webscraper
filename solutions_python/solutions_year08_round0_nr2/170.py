import re

def first(lst): return lst[0]

f = open('B-large.in')

n = int(f.readline())
for i in range(n):
    froma = []
    fromb = []
    traina = []
    trainb = []

    t = int(f.readline())
    nab = re.findall("\d+",f.readline())
    na, nb = int(nab[0]), int(nab[1])
    aa = 0
    bb = 0

    for a in range(na):
        s = map(int,re.findall("\d\d",f.readline()))
        froma.append([s[0]*60 + s[1],s[2]*60+s[3]])
    for b in range(nb):
        s = map(int,re.findall("\d\d",f.readline()))
        fromb.append([s[0]*60 + s[1],s[2]*60+s[3]])

    froma.sort(key = first)
    fromb.sort(key = first)

    # chuse next line
    while(froma or fromb):
        if froma and fromb and \
           froma[0][0] <= fromb[0][0]:
               if traina and traina[0] <= froma[0][0]:
                   del traina[0]
                   trainb.append(froma[0][1] + t)
                   trainb.sort()
                   del froma[0]
               else:
                    aa = aa + 1
                    trainb.append(froma[0][1] + t)
                    trainb.sort()
                    del froma[0]
        elif froma and fromb:
            if trainb and trainb[0] <= fromb[0][0]:
                del trainb[0]
                traina.append(fromb[0][1] + t)
                traina.sort()
                del fromb[0]
            else:
                bb = bb + 1
                traina.append(fromb[0][1] + t)
                traina.sort()
                del fromb[0]
        elif froma:
            if traina and traina[0] <= froma[0][0]:
               del traina[0]
               trainb.append(froma[0][1] + t)
               trainb.sort()
               del froma[0]
            else:
                aa = aa + 1
                trainb.append(froma[0][1] + t)
                trainb.sort()
                del froma[0]
        else:
            if trainb and trainb[0] <= fromb[0][0]:
                del trainb[0]
                traina.append(fromb[0][1] + t)
                traina.sort()
                del fromb[0]
            else:
                bb = bb + 1
                traina.append(fromb[0][1] + t)
                traina.sort()
                del fromb[0]

    print 'Case #%d: %d %d' % (i+1, aa, bb)
