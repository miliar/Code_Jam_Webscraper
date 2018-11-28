dico = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
nb = int(raw_input())
if nb:
    for i in range(nb):
        data = raw_input()
        s = ""
        for j in data:
            if j in dico:
                s += dico[j]
            else:
                s += j
        print 'Case #{0}: {1}'.format(i + 1, s)

