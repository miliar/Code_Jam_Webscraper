
def translate(line):

    assoctable = {'a':'y', 'b':'h', 'c':'e', 'd':'s',
                  'e':'o', 'f':'c', 'g':'v', 'h':'x',
                  'i':'d', 'j':'u', 'k':'i', 'l':'g',
                  'm':'l', 'n':'b', 'o':'k', 'p':'r',
                  'q':'z', 'r':'t', 's':'n', 't':'w',
                  'u':'j', 'v':'p', 'w':'f', 'x':'m',
                  'y':'a', 'z':'q' }

    translation = ''
    for l in line:
        if l != " " and l!='\n':
            translation += assoctable[l]
        else:
            translation += l

    return translation


def test(filename):
    fin = open(filename, 'r')
    fout = open(filename[:len(filename)-3] + ".out", 'w')
    T = int(fin.readline())
    for k in range(T):
        line = fin.readline()
        transline = translate(line)
        fout.write("Case #%d: %s" % (k+1,transline))
        
    fin.close()
    fout.close()


#main
test('A-small-attempt0.in')
        
