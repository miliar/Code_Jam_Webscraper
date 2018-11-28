def translate(text):
    dico = {
            'a':'y',
            'b':'h',
            'c':'e',
            'd':'s',
            'e':'o',
            'f':'c',
            'g':'v',
            'h':'x',
            'i':'d',
            'j':'u',
            'k':'i',
            'l':'g',
            'm':'l',
            'n':'b',
            'o':'k',
            'p':'r',
            'q':'z',
            'r':'t',
            's':'n',
            't':'w',
            'u':'j',
            'v':'p',
            'w':'f',
            'x':'m',
            'y':'a',
            'z':'q',
            ' ':' ',
    }
    s = ""
    for i in xrange(len(text)):
        s += dico[text[i]]

    return s

nb = int(raw_input())
lines = [raw_input() for _ in xrange(nb)]
for i in xrange(nb):
    print "Case #%s: %s"%(i+1, translate(lines[i]))
