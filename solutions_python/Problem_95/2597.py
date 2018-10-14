
t ={'a':'y', 'b':'h', 'c':'e', 'd':'s',
    'e':'o', 'f':'c', 'g':'v', 'h':'x',
    'i':'d', 'j':'u', 'k':'i', 'l':'g',
    'm':'l', 'n':'b', 'o':'k', 'p':'r',
    'q':'z', 'r':'t', 's':'n', 't':'w',
    'u':'j', 'v':'p', 'w':'f', 'x':'m',
    'y':'a', 'z':'q', ' ':' ', '\n':'\n',
    '1':'1', '2':'2', '3':'3', '4':'4',
    '5':'5', '6':'6', '7':'7', '8':'8',
    '9':'9', '0':'0'}

f1 = open('A-small-attempt1.in')
f2 = open('rez.txt', 'w')

line = f1.readline()
line = f1.readline()
newline = ''
n = 1
while(line != ''):
    newline = "Case #%d: " % n
    n = n + 1
    for i in line:
        newline = newline + t[i]
    f2.write(newline)
    
    line = f1.readline()

f1.close()
f2.close()
        
