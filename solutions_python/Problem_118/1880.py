import re,math

def palindrom(szam):
    szoveg = str(szam)
    for i in range(len(szoveg) / 2):
        if szoveg[i] != szoveg[len(szoveg) - i - 1]:
            return False
    return True

def keszit(szam):
    szoveg = list(str(szam))
    for i in range(len(szoveg) / 2):
        szoveg[len(szoveg) - i - 1] = szoveg[i]
    return int("".join(szoveg))

def novelj(karakterlista,eltolas=0):   
    hossz = len(karakterlista)
    fent = hossz / 2 + eltolas
    lent = hossz / 2 - eltolas
    if hossz % 2 == 0:
        lent -= 1
    if lent < 0:
        new_list = ["0" for i in range(hossz-1)]
        new_list.insert(0,"1")
        new_list.append("1")
        return int("".join(new_list))
    new_digit = (int(karakterlista[fent]) + 1) % 10
    karakterlista[fent] = str(new_digit)
    karakterlista[lent] = str(new_digit)
    if new_digit == 0:
        return novelj(karakterlista,eltolas+1)
    return int("".join(karakterlista))

def kovetkezo(szam):
    if not palindrom(szam):
        return keszit(szam)
    return novelj(list(str(szam)))


def mennyi(lent,fent):
    db = 0
    akt = kovetkezo(lent) if not palindrom(lent) else lent
    print "starting at %d" % lent
    while akt <= fent:
        gyok = math.sqrt(akt)
        egeszgyok = int(gyok)
        if akt >= lent and palindrom(egeszgyok) and egeszgyok == gyok:
            print "%d ok" % akt
            db += 1
        else:
            pass
        akt = kovetkezo(akt)
    print "vege: %d" % fent
    return db

def olvas(f):
    bounds = re.split(" ",f.readline())
    return mennyi(long(bounds[0]),long(bounds[1]))


def main():
    ki = []
    with open("C-small-attempt0.in","r") as f:
        probak = f.readline()
        for i in range(int(probak.strip())):
            kisor = "Case #%d: %s" % (i+1, olvas(f))
            print kisor
            ki.append(kisor)
    with open("fairsquare.out","w") as f:
        f.write("\n".join(ki))

if __name__ == "__main__":
    main()
