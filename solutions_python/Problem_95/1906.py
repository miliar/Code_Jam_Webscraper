#Google Googlerese

d = {
    'e':'o',
    'j':'u',
    'p':'r',
    'm':'l',
    'y':'a',
    's':'n',
    'l':'g',
    'c':'e',
    'k':'i',
    'd':'s',
    'x':'m',
    'v':'p',
    'n':'b',
    'r':'t',
    'i':'d',
    'b':'h',
    't':'w',
    'a':'y',
    'h':'x',
    'w':'f',
    'f':'c',
    'u':'j',
    'o':'k',
    'g':'v',
    'z':'q',
    'q':'z'
    }

def translate(s):
    temp = []
    for i in s:
        if i == ' ':
            temp.append(' ')
        else:
            temp.append(d[i])
    word =  ''.join([letter for letter in temp])
    return word
            
            

f = open('Google Googlerese.in','r')
g = open('Google Googlerese.out','w')

cases = int(f.readline())

for i in range(cases):
    s= f.readline().rstrip()
    g.write("Case #%s: %s\n" %(str(i+1),translate(s)))
print "Done."
g.close()










    
