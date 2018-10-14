fn = 'A-small-attempt0'
f = open('%s.in' % fn, 'r')
o = open('%s.out' % fn, 'w')

tests = int(f.readline().strip())

trans = {
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

for test in xrange(tests):
    l = list(f.readline().strip())
    res = [trans[i] for i in l]
    s = "Case #%d: %s\n" % (test+1, ''.join(res))
    print s
    o.write(s)