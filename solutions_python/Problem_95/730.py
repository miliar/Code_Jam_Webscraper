d = {'\n': '\n',' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q': 'z'}
f = open('input', 'rU')
f2 = open('output', 'w')
r = ''
for i in range(int(f.readline())):
    r+='Case #' + str(i+1) + ': '
    for c in f.readline():
        r+=d[c]
f2.write(r)
f.close()
f2.close()