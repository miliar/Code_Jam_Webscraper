trt = {'a':'y',
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
       }

def translate(text):
    ret = '';
    for ch in text:
       ret += trt[ch];
    return ret;

i=1;
f = open('inp.in','r');
f2 = open('out.out','r+');
nr = int(f.readline());
while i<=nr:
    #print ('Case #' + str(i) + ': ' + translate(f.readline()[:-1]));
    f2.write('Case #' + str(i) + ': ' + translate(f.readline()[:-1]) + '\n');
    i = i + 1;
f2.close();
