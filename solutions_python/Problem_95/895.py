import sys

mapping = {'a':'y',
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
           'z':'q',}

count = int(sys.stdin.readline())
for i in range(count):
    out = ''
    s = sys.stdin.readline()[:-1]
    for c in s:
        if c in mapping:
            out = out + mapping[c]
        else:
            out = out + c
    print("Case #"+str(i+1)+": "+out)
