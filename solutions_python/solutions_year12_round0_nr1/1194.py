T = int(raw_input())

map = {'a':'y',
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
       'q':'z', # only one left
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

for c in range(T):
    case = "Case #%d:" % (c+1)
    
    line = raw_input()
    letters = list(line)
    trans = []
    
    for ch in letters: trans.append(map[ch])
    trans = ''.join(trans)
    print "%s %s" % (case, trans)