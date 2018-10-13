f = open("A-small-attempt0.in")
f2 = open("out.txt","w")
d = {' ':' ','y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f', 'l':'g', 'b':'h', 'k':'i', 'u':'j', 'o':'k', 'm':'l', 'x':'m', 's':'n', 'e':'o', 'v':'p', 'z':'q', 'p':'r', 'd':'s', 'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x', 'a':'y', 'q':'z'}


def to_eng(foo):
    return "".join([d[x] for x in list(foo)])
        

n = int(f.readline())
for i in range(n):
    q = f.readline()[:-1]
    f2.write( "Case #%d: %s\n" % (i+1,to_eng(q)))
f2.close()

    
