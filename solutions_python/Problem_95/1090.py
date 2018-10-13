code = {
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
    'z': 'q'
        }
code = dict((v,k) for k,v in code.iteritems())
if __name__ == '__main__':
    inp = file('A-small-attempt0.in','r')
    out = file('A-small.out', 'w')
    n = int(inp.readline())
    i = 1
    for line in inp:
        trs = []
        words = line.split()
        for word in words:
            tw = ''
            for c in word:
                tw += code[c]
            trs.append(tw)
        out.write('Case #%d: %s\n' % (i, ' '.join(trs)))
        i += 1

