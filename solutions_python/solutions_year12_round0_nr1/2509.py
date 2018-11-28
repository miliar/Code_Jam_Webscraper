import string
f = open('/home/david/Downloads/A-small-attempt2.in', 'r+')

decode = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}

froma = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
to =    ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']
fro = 'abcdefghijklmnopqrstuvwxyz '
tok = 'yhesocvxduiglbkrztnwjpfmaq '
trans = string.maketrans(fro,tok)
f.readline()
linesT = f.readlines()
for k in range(len(linesT)):
    linesT[k]=linesT[k].rstrip('\n')
    print 'Case #'+ str(k+1)+ ': ' + linesT[k].translate(trans)
