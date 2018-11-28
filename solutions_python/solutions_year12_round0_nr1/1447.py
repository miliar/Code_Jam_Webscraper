rep = {
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
'z':'q'
}

num = int(raw_input())
i = 1
while i <= num:
    line = raw_input()
    newline = []
    for char in line:
        if char in rep:
            newline.append(rep[char])
        else:
            newline.append(char)
    print 'Case #%s:' % i,
    print ''.join(newline)
    i += 1



















