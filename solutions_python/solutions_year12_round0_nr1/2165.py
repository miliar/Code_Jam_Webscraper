tab = {' ': ' ', '\n': '\n', 'y': 'a', 'n': 'b', 'f': 'c', 'i': 'd', 'c': 'e', 'w': 'f', 'l': 'g', 'b': 'h', 'k': 'i', 'u': 'j', 'o': 'k', 'm': 'l', 'x': 'm', 's': 'n', 'e': 'o', 'v': 'p', 'z': 'q', 'p': 'r', 'd': 's', 'r': 't', 'j': 'u', 'g': 'v', 't': 'w', 'h': 'x', 'a': 'y', 'q': 'z'}

fi = open('./A.in', 'r')
fo = open('./A.out', 'w')
sz = int(fi.readline())
for i in range(sz):
    fo.write('Case #%i: ' % (i + 1))
    for c in fi.readline():
        fo.write(tab[c])
fo.close()
fi.close()
