mydict = {
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
    'q': 'z',
    ' ': ' ',
    '\n': '\n'
}

def myfunc(infile):
    lineno = -1
    mystr = ""
    for line in open(infile, 'r'):
        lineno = lineno + 1
        if lineno == 0: continue
        mystr += "Case #%d: " % (lineno)
        for c in line:
            mystr += mydict[c]
    return mystr
            
print myfunc('A-small-attempt0.in')
