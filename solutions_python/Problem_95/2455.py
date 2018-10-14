# Google Code Jam
# Googlerese
# vishen

# q = (d, z)
# i = (d, z)
mapping = {
    ' ': ' ',
    'a': 'y',
    'b': 'n',
    'c': 'f',
    'e': 'c',
    'f': 'w',
    'g': 'l',
    'h': 'b',
    'i': 'k',
    'j': 'u',
    'k': 'o',
    'l': 'm',
    'm': 'x',
    'n': 's',
    'o': 'e',
    'p': 'v',
    'q': 'z',
    'r': 'p',
    's': 'd',
    't': 'r',
    'u': 'j',
    'v': 'g',
    'w': 't',
    'x': 'h',
    'y': 'a',
    'z': 'q',
    'd': 'i',
}

reverse_mapping = {}
for k, v in mapping.items():
    reverse_mapping[v] = k

f = open('google_dump.txt', 'r')
T = f.readline()
count = 0
gs = open('google_solutions.txt', 'w')
for x in range(int(T)):
    G = f.readline()
    S = ''
    for letter in G:
        try:
            S = '%s%s' % (S, reverse_mapping[letter])
        except KeyError:
            pass

    gs.write('Case #%d: %s\n' % (x+1, S))

f.close()


