f = open('A-small-attempt0.in','r')
r = open('A-small-attempt0.out','w')

magicleetcode = {
'y': 'a',
'n': 'b',
'f': 'c',
'i': 'd',
'c': 'e',
'w': 'f',
'l': 'g',
'b': 'h',
'k': 'i',
'u': 'j',
'o': 'k',
'm': 'l',
'x': 'm',
's': 'n',
'e': 'o',
'v': 'p',
'z': 'q',
'p': 'r',
'd': 's',
'r': 't',
'j': 'u',
'g': 'v',
't': 'w',
'h': 'x',
'a': 'y',
'q': 'z'
}

f.readline()
i = 1

for l in f:
    r.write("Case #%d: " % i)
    for c in l:
        if c in magicleetcode:
            r.write(magicleetcode[c])
        else:
            r.write(c)
    i += 1

