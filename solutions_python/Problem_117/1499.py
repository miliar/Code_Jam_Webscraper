import re

def jatekbe(f):
    dimenziok = re.split(" ",f.readline())
    x,y = int(dimenziok[1]), int(dimenziok[0])    
    sorok = []
    for i in range(y):
        vonal = f.readline()
        szamok = [int(x.strip()) for x in re.split(" ",vonal)]
        sorok.append(szamok)
    return sorok

def jatek_ell(sorok):
    max_oszlop = [max(x) for x in sorok]
    oszlopok = [[sorok[i][j] for i in range(len(sorok))] for j in range(len(sorok[0]))]
    oszlop_maxok = [max(x) for x in oszlopok]
    for i in range(len(sorok)):
        for j in range(len(sorok[i])):
            temp = sorok[i][j]
            if temp != max_oszlop[i] and temp != oszlop_maxok[j]:
                return "NO"
    return "YES"
        
def main():
    ki = []
    with open("B-large.in","r") as f:
        probak = f.readline()
        for i in range(int(probak.strip())):
            state = jatekbe(f)
            kisor = "Case #%d: %s" % (i+1, jatek_ell(state))
            print kisor
            ki.append(kisor)
    with open("sorok2.out","w") as f:
        f.write("\n".join(ki))


if __name__ == "__main__":
    main()
