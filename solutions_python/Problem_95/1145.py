'''
Created on May 6, 2011

@author: jirasak
'''

def solve(i, line):
    theString = '''ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv
our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'''
    mapping = {'e':'o',
                'j':'u',
                'p':'r',
                'm':'l',
                'y':'a',
                's':'n',
                'l':'g',
                'c':'e',
                'k':'i',
                'd':'s',
                'k':'i',
                'x':'m',
                'v':'p',
                'e':'o',
                'd':'s',
                'k':'i',
                'n':'b',
                ' ':' ',
                'r':'t',
                'e':'o',
                ' ':' ',
                'j':'u',
                's':'n',
                'i':'d',
                'c':'e',
                'p':'r',
                'd':'s',
                'r':'t',
                'y':'a',
                's':'n',
                'i':'d',
                'r':'t',
                'b':'h',
                'c':'e',
                'p':'r',
                'c':'e',
                ' ':' ',
                'y':'a',
                'p':'r',
                'c':'e',
                ' ':' ',
                'r':'t',
                't':'w',
                'c':'e',
                's':'n',
                'r':'t',
                'a':'y',
                ' ':' ',
                'd':'s',
                'k':'i',
                'h':'x',
                ' ':' ',
                'w':'f',
                'y':'a',
                'f':'c',
                'r':'t',
                'e':'o',
                'p':'r',
                'k':'i',
                'y':'a',
                'm':'l',
                ' ':' ',
                'v':'p',
                'e':'o',
                'd':'s',
                'd':'s',
                'k':'i',
                'n':'b',
                'k':'i',
                'm':'l',
                'k':'i',
                'r':'t',
                'k':'i',
                'c':'e',
                'd':'s',
                'd':'s',
                'e':'o',
                ' ':' ',
                'k':'i',
                'r':'t',
                ' ':' ',
                'k':'i',
                'd':'s',
                ' ':' ',
                'e':'o',
                'o':'k',
                'y':'a',
                'a':'y',
                ' ':' ',
                'k':'i',
                'w':'f',
                ' ':' ',
                'a':'y',
                'e':'o',
                'j':'u',
                ' ':' ',
                't':'w',
                'y':'a',
                's':'n',
                'r':'t',
                'u':'j',
                ' ':' ',
                'r':'t',
                'e':'o',
                ' ':' ',
                'j':'u',
                'd':'s',
                'r':'t',
                ' ':' ',
                'l':'g',
                'k':'i',
                'g':'v',
                'c':'e',
                ' ':' ',
                'j':'u',
                'v':'p',
                'z':'q',
                'q':'z'}
#    for i in range(len(theString.splitlines()[0])):
#        a = theString.splitlines()[0][i]
#        b = theString.splitlines()[1][i]
#        print "'%s':'%s'," % (a, b)
#    print sorted(mapping.keys())
#    print sorted(mapping.values())
    outString = ''
    for c in line:
        outString += mapping[c]
    return outString

if __name__ == '__main__':
    fIn = file('A-small-attempt0.in')
    inLines = fIn.readlines()
    fIn.close()
    
    inLines = inLines[1:]
    numLines = len(inLines)
    i = 0
    while i < numLines:
        line = inLines[i].strip()
        i += 1
        data = solve(i, line)
        print 'Case #%s: %s' % (i, data)
    