import sys

def translator(G):
    mappings = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x',
        'i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z',
        'r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q',
        ' ':' '}
    S = ''.join([mappings[c] for c in G])
    return S

def process(num, fin, fout):
    g = fin.readline().strip()
    s = translator(g)
    fout.write("Case #%d: %s\n" % (i+1, s))
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Please indicate input and output"
    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[2], 'w')
    N = int(fin.readline())
    for i in xrange(N):
        process(i, fin, fout)
    fin.close()
    fout.close()
    print " *** Translation Done ***"