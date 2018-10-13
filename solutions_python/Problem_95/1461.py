d = {' ':' ','a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r', 'q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}

def translate(s):
    return ''.join([d[i] for i in s])

tests = int(raw_input())
for i in xrange(tests):
    print 'Case #%s:' % (i+1), translate(raw_input())

