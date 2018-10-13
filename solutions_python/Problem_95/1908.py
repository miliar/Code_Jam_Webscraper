g = {'a':'y','b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q', ' ':' ','\n':''}

f= open("A-small-attempt0.in","r")
t= int(f.readline())
input = []
for i in range(0,t):
    input.append(f.readline())

f.close()
f = open("output.out","w")

def googlerese():
    cont = 1
    for i in input:
        out = ""
        for letter in i:
            out += g[letter]
        f.write("Case #%s: %s \n" % (cont,out))
        cont+=1
    f.close()

googlerese()
