from string import maketrans

D = {
        'a': 'y',
        'b': 'h',
        'c': 'e',
        'd': 's',
        'e': 'o',
        'f': 'c',
        'g': 'v',
        'h': 'x',
        'i': 'd',
        'j': 'u',
        'k': 'i',
        'l': 'g',
        'm': 'l',
        'n': 'b',
        'o': 'k',
        'p': 'r',
        'q': 'z',
        'r': 't',
        's': 'n',
        't': 'w',
        'u': 'j',
        'v': 'p',
        'w': 'f',
        'x': 'm',
        'y': 'a',
        'z': 'q'
    }
transTable = maketrans(''.join(D.keys()), ''.join(D.values()))

def trans(s, table):
    return s.translate(table)


if __name__ == '__main__':
    import sys
    infile = sys.argv[1]
    f = open(infile)
    T = int(f.readline().strip())
    for i in range(T):
        ln = f.readline().strip()
        print 'Case #%d: %s'%(i+1, trans(ln, transTable))
