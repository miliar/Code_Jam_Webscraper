def compatible(a,b):
    if a==b:
        return False
    if a == "V" and(b=="R" or b == "B"):
        return False
    if a == "G" and(b=="Y" or b == "B"):
        return False
    if a == "O" and(b=="R" or b == "Y"):
        return False
    return True


T = int(input())
for uniqueindice in range(T):
    liste = list(map(int, input().split()))
    lettre = ["R","O","Y","G","B","V"]
    liste2 = []
    lettre2 = []
    for i in range(1, len(liste)):
        if liste[i] != 0:
            liste2 += [liste[i]]
            lettre2 += [lettre[i-1]]




    mot = lettre2[0]
    liste2[0]-= 1
    i = 0
    impossible = False

    while any(e != 0 for e in liste2) and not impossible:
        liste2, lettre2 = (list(t) for t in zip(*sorted(zip(liste2, lettre2))))
        liste2 = list(reversed(liste2))
        lettre2 = list(reversed(lettre2))

        if liste2[i] != 0 and compatible(mot[-1], lettre2[i]) and compatible(lettre2[i], mot[-1]):
            liste2[i] -= 1
            mot = mot + lettre2[i]
            i = 0
        else:
            i += 1

        if i >= len(liste2):
            impossible = True

    #print(mot)
    print("Case #{}:".format(uniqueindice+1), end = " ")
    if impossible or (len(mot) != 1 and (not compatible(mot[0], mot[-1] or not compatible(mot[-1], mot[0])))):
        print("IMPOSSIBLE")
    else:
        print(mot)
