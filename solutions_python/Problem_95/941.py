e2g = {
  'a':'y','b':'n','c':'f','d':'i','e':'c','f':'w','g':'l',
  'h':'b','i':'k','j':'u','k':'o','l':'m','m':'x','n':'s',
  'o':'e','p':'v','q':'z','r':'p','s':'d','t':'r',
  'u':'j','v':'g','w':'t','x':'h','y':'a','z':'q',
  ' ':' '
}
g2e = {}
for l in e2g:
    g2e[e2g[l]] = l

fn = 'A-small-attempt0'
fi = open('%s.in' % fn, 'r')
fo = open('%s.out' % fn, 'w')

t = int(fi.readline())
cases = fi.readlines()
fi.close()

for i in range(t):
    fo.write('Case #%s: ' % (i + 1))
    for letter in cases[i].strip():
	fo.write(g2e[letter])
    fo.write('\n')

fo.close()
