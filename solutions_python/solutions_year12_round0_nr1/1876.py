#!/usr/bin/python
    
def analyze(filename):
    f = open(filename)
    noLines = int(f.readline())

    count = 1
    for i in range (noLines):
        line = f.readline()
        print 'Case #{num}: '.format(num = count) + "".join([convert(x)+" " for x in line.split()])
        count = count + 1

def convert(token):
    googlereseToEnglish = {
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
    tokenList = list(token)
    newList = [googlereseToEnglish[x] for x in tokenList]
    return "".join(newList)

analyze('input')
