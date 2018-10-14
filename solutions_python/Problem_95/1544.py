import sys

dic = {
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
}

n = int(sys.stdin.readline())
for i in range(n):
    line = sys.stdin.readline()
    line = line[:-1]
    output = 'Case #'+str(i+1)+': '
    for c in line:
        if c >= 'a' and c <= 'z':
            output = output + dic[c]
        else:
            output = output + c
    print output
