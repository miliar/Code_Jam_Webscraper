import re
import psyco
psyco.full()

def signal2regex(s):
    output = []
    i = 0
    while i < len(s):
        if s[i] == '(':
            output.append('(')
            i = i+1
            suboutput = []
            while s[i] != ')':
                suboutput.append(s[i])
                i = i+1
            output.append('|'.join(suboutput))
            output.append(')')
            i = i+1
        else:
            output.append(s[i])
            i = i+1
   
    output.append(r'\Z') 
    return ''.join(output)


def parseInput(f):
    lines = open(f).readlines()
    letras, palabras, casos = [int(x) for x in lines[0].split()]
    lenguaje = []
    for k in range(palabras):
        lenguaje.append(lines[1+k].strip())
    
    seniales = []
    for k in range(casos):
        seniales.append(lines[1+palabras+k].strip())

    return lenguaje, seniales


if __name__ == '__main__':
    lenguaje, seniales = parseInput('input.txt')
    i = 1
    for s in seniales:
        r = re.compile(signal2regex(s))
        matches = 0
        for p in lenguaje:
            if r.match(p) != None:
                matches = matches + 1
        print "Case #%s: %s" % (i, matches)
        i = i + 1
    #for i in range(500):
    #    print i
    #    for j in range(5000):
    #        r = re.compile(signal2regex('a(abc)der(ukz)(dyz)(abc)(uv)asdkwx'))
    #        r.match('acderkybvasdkwx')

#r = re.compile(signal2regex('aa(abc)(bad)d'))
#print r.match('aacda')
