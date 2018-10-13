import os
import fileinput

#googlerese - english
gMap = {
    'y':'a',
    'n':'b',
    'f':'c',
    'i':'d',
    'c':'e',
    'w':'f',
    'l':'g',
    'b':'h',
    'k':'i',
    'u':'j',
    'o':'k',
    'm':'l',
    'x':'m',
    's':'n',
    'e':'o',
    'v':'p',
    'z':'q',
    'p':'r',
    'd':'s',
    'r':'t',
    'j':'u',
    'g':'v',
    't':'w',
    'h':'x',
    'a':'y',
    'q':'z'
}

def decode(s=None):
    o = ''
    for c in s:
        if gMap.has_key(c):
            o += gMap[c]
        else:
            o += c
    return o


if __name__ == '__main__':
    r = []
    filename = None

    for test in fileinput.input():
        if not fileinput.isfirstline():
            s = 'Case #%d: %s' % (fileinput.lineno()-1, decode(test))
            r.append(s)
        else:
            filename = fileinput.filename()

    if filename:
        f = open(os.path.join(os.path.dirname(filename), 'output.txt'), 'w')
        f.writelines(r)
