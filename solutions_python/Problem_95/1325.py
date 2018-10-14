fl = open('A-small-attempt0.in','r')
case=int(fl.readline())
d={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c',
   'g':'v','h':'x','i':'d','j':'u','k':'i','l':'g',
   'm':'l','n':'b','o':'k','p':'r','q':'z','r':'t',
   's':'n','t':'w','u':'j','v':'p','w':'f','x':'m',
   'y':'a','z':'q','\n':'\n',' ':' '}
for j in range(case):
    z=list(fl.readline())
    for i in range(len(z)):
        z[i]=d[z[i]]
    z=''.join(z)
    print "Case #%d:"%(j+1),z,
        

