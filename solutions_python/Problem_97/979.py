def memeChiffre(chaine1, chaine2):
    buf1 = chaine1
    if len(chaine1) != len(chaine2):
        return False
    for c in chaine2:
        i = 0
        pareil = False
        while i < len(buf1):
            if c == buf1[i]:
                buf1 = buf1[:i] + buf1[(i + 1):]
                pareil = True
                break
            i += 1
        if pareil == False:
            return False
    return True



if __name__ == "__main__":
    with open('C-small-attempt0.in','r') as f:
        sortie = open('sortie.txt','w')
        nbLigne = 0
        for ligne in f:
            if nbLigne != 0:
                buf = ligne.split()
                A = int(buf[0])
                B = int(buf[1])
                res = 0
                listeA = []
                while A < B:
                    listeB = range((A + 1), (B + 1))
                    for b in listeB:
                        chA = str(A)
                        chb = str(b)
                        i = 1
                        if chA != chb:
                            while i < len(chA):
                                if chA[i:] + chA[:i] == chb:
                                    res += 1
                                    print("{0}, {1}, {2}".format(chA, chb, chA[i:] + chA[:i]))
                                    break
                                i += 1
                            
                    A += 1
                print("Case #{0}: {1}".format(nbLigne, res))
                sortie.write("Case #{0}: {1}\n".format(nbLigne, res))
            nbLigne += 1
    sortie.close()
    print("termine")
