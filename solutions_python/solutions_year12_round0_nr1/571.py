import sys, re

cmap = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}

input = sys.stdin
T = int(input.readline())
for t in xrange(T):
    line = input.readline().strip()
    def translate(match):
        return cmap[match.group(0)]
    print "Case #%d: %s" % (t + 1, re.sub('|'.join(cmap), translate, line))

