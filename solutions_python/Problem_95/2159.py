
awesome = {
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
'\n':'\n'
}

def trans(string):
    translation = []
    for i in range(0, len(string)):
        translation.append( awesome[string[i]] )
    return translation

def main():
    f = open('/home/nikita/input.txt', 'r')
    f2 = open('/home/nikita/out.txt', 'w')
    print f
    num = int(f.readline())
    for i in range(1, num+1):
        text = f.readline()
        out = trans(text)
        f2.write("Case #" +str(i) + ": " + "".join(out))
    
main()