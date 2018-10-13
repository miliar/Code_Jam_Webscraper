#f=open('test.in','r')
f=open('A-small-attempt0.in','r')
r=open('result.txt','w')
dic={
    'y':'a',
    'n':'b',
    'f':'c',
    'i':'d',
    'c':'e',
    'w':'f',
    'l':'g',
    'b':'h',
    'k':'i',
    'u':'j',
    'o':'k',
    'm':'l',
    'x':'m',
    's':'n',
    'e':'o',
    'v':'p',
    'z':'q',
    'p':'r',
    'd':'s',
    'r':'t',
    'j':'u',
    'g':'v',
    't':'w',
    'h':'x',
    'a':'y',
    'q':'z',
    ' ':' ',
    '\n':'\n'}

T=int(f.readline())
t=0
for i in range(T):
    line = f.readline()
    t+=1
    r.write('Case #'+str(t)+': ')
    for j in range(len(line)):
        #print dic[line[j]]
        r.write(dic[line[j]])
    

f.close()
r.close()
