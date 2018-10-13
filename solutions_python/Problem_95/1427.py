"""
Find correct encoding...
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv

Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
"""
import sys
TRANSLATE_MAP = {
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
    ',':',',
    ' ':' ',
}

def transformer(x):
    return TRANSLATE_MAP.get(x, '')

def mapper(x):
    return transformer(x)

def run(f):
    testcases = f.next()
    for i, line in enumerate(f):
        print 'Case #%s:' % (i +1), ''.join(map(mapper, line))

if __name__ == "__main__":
    assert transformer('a') == 'y'
    assert transformer('z') == 'q'
    f = open(sys.argv[1])
    run(f)
    f.close()
