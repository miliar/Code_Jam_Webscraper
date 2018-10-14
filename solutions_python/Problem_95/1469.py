import sys

f = map(str.strip, open(sys.argv[1], 'rb').readlines(), "\n")
n = int(f.pop(0))

mapping = {'y':'a',
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
           'z':'q', #
           'p':'r',
           'd':'s',
           'r':'t',
           'j':'u',
           'g':'v',
           't':'w',
           'h':'x',
           'a':'y',
           'q':'z'} #
#for i in sorted(mapping.keys()):
#    print (ord(i) - ord('a')), ":", (ord(mapping[i]) - ord('a'))

def translate(s):
    out = ""
    for i in s:
        if i is not ' ': out += mapping[i]
        else: out += ' '
    return out
    

for i in range(n):
    print "Case #%s: %s" % (i+1, translate(f[i]))
