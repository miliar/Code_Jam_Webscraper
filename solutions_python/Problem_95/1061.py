with open('A-small-attempt0.in', 'r') as f:
    sortie = open('sortie.txt','w')
    nbLigne = 0
    dic = {'a': 'y','b': 'h','c': 'e','d': 's','e': 'o','f': 'c','g': 'v','h': 'x','i': 'd','j': 'u','k': 'i','l': 'g','m': 'l','n': 'b','o': 'k','p': 'r','q': 'z','r': 't','s': 'n','t': 'w','u': 'j','v': 'p','w': 'f','x': 'm','y': 'a','z': 'q','\n':''}
    for ligne in f:
        if nbLigne != 0:
            buf = ""
            for c in ligne:
                if c == ' ':
                    buf += ' '
                else:
                    buf += dic[c]
            print("Case #{0}: {1}".format(nbLigne, buf))
            sortie.write("Case #{0}: {1}\n".format(nbLigne, buf))
        nbLigne += 1
    sortie.close()
