'''
Created on Apr 14, 2012

@author: Russell
'''
import sys
m = {   ' ':' ',
        'a':'y',
        'c':'e',
        'b':'h',
        'e':'o',
        'd':'s',
        'g':'v',
        'f':'c',
        'i':'d',
        'h':'x',
        'k':'i',
        'j':'u',
        'm':'l',
        'l':'g',
        'o':'k',
        'n':'b',
        'q':'z',
        'p':'r',
        's':'n',
        'r':'t',
        'u':'j',
        't':'w',
        'w':'f',
        'v':'p',
        'y':'a',
        'x':'m',
        'z':'q',
        '\n':''
}
def solve(fn):
    f = open(fn)
    lines = f.readlines();
    f.close();
    nc = int(lines[0])
    for i in range (1, nc + 1):
        line = lines[i]
        nline = ''
        for w in line:
            nline += m[w]
        print 'Case #%d: %s' % (i, nline)
        
if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            solve(fn)

    
    
