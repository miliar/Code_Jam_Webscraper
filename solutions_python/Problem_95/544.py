from sys import stdout
tbl = {
    'a': 'y',
    'b': 'n',
    'c': 'f',
    'd': 'i',
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
    ' ': ' '
    }
tbl = dict((v,k) for k, v in tbl.iteritems())
fin = file('A-small-attempt0.in', 'r')
fout = file('A-small0.out', 'w')
T = int(fin.readline())
for t in range(1, T+1):    
    fout.write('Case #' + str(t) + ': ')
    s = fin.readline()
    for c in str.strip(s):
        fout.write(tbl[c])
    fout.write('\n')
fout.flush()
fin.close()
fout.close()
