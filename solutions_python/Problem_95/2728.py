def makeDict():
    d = dict()
    d['a'] = 'y'
    d['b'] = 'h'
    d['c'] = 'e'
    d['d'] = 's'
    d['e'] = 'o'
    d['f'] = 'c'
    d['g'] = 'v'
    d['h'] = 'x'
    d['i'] = 'd'
    d['j'] = 'u'
    d['k'] = 'i'
    d['l'] = 'g'
    d['m'] = 'l'
    d['n'] = 'b'
    d['o'] = 'k'
    d['p'] = 'r'
    d['q'] = 'z'
    d['r'] = 't'
    d['s'] = 'n'
    d['t'] = 'w'
    d['u'] = 'j'
    d['v'] = 'p'
    d['w'] = 'f'
    d['x'] = 'm'
    d['y'] = 'a'
    d['z'] = 'q'
    d[' '] = ' '
    return d

def readFile(fileName,d):
    c=0
    for line in open(fileName):
        if c==0:
            c=1
        else:
            print('Case #',c,': ',translate(line.strip(),d), sep='')
            c+=1
        
def translate(line,d):
    r = ""
    for l in line:
        r+=d[l]
    return r

def main():
    d = makeDict()
    fileName = input("File name: ")
    readFile(fileName,d)
    

main()
