mapa = {
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
    ' ':' '
 }
def traducir(strange_phrase):
    word=''
    for a in strange_phrase:
        word = word + mapa[a]
    return word

archi= open ("A-small-attempt0.in", 'r')
salida = open('output.dat','w')
cases = int(archi.readline().split()[0])
for i in range (cases):
    label = "Case #" + str(i+1) + ": "
    phrase = archi.readline().replace('\n','')
    result = traducir(phrase)
    label = label + result + '\n'
    salida.writelines(label)

