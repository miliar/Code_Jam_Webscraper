mapping = {
           'a':'y',
           'b':'n',
           'c':'f',
           'd':'i',
           'e':'c',
           'f':'w',
           'g':'l',
           'h':'b',
           'i':'k',
           'j':'u',
           'k':'o',
           'l':'m',
           'm':'x',
           'n':'s',
           'o':'e',
           'p':'v',
           'q':'z',
           'r':'p',
           's':'d',
           't':'r',
           'u':'j',
           'v':'g',
           'w':'t',
           'x':'h',
           'y':'a',
           'z':'q'}

rev_map = {}
for k,v in mapping.items():
    rev_map[v] = k

def translate(inp):
    res = []
    for c in inp:
        if c == ' ':
            res.append(' ')
        else:
            res.append(rev_map[c])
    return ''.join(res)

for case in xrange(input()):
    inp = raw_input()
    
    res = translate(inp)
    
    print "Case #%i: %s" % (case+1, res)