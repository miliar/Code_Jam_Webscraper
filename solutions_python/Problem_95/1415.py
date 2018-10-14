import sys

chars = {
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
    'p':'r',
    's':'n',
    'r':'t',
    'u':'j',
    't':'w',
    'w':'f',
    'v':'p',
    'y':'a',
    'x':'m',
    'q':'z',
    'z':'q',
    ' ':' '
}
            
first_line = sys.stdin.readline()
n = int(first_line)

for i in xrange(n):
    line = sys.stdin.readline()
    res = ""
    for c in xrange(len(line)-1):
        res += chars[line[c]]
    print "Case #"+ str(i+1) +": " + res
