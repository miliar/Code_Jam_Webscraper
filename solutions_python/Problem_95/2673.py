import sys
gabage = raw_input()
i = 1 

table = {'a':'y', 'b':'h', 'c':'e', 'd':'s',
        'e':'o', 'f':'c', 'g':'v', 'h':'x',
        'i':'d', 'j':'u', 'k':'i', 'l':'g',
        'm':'l', 'n':'b', 'o':'k', 'p':'r',
        'q':'z', 'r':'t', 's':'n', 't':'w',
        'u':'j', 'v':'p', 'w':'f', 'x':'m',
        'y':'a', 'z':'q', ' ':' ', '\n':''}

def transrate(text):
    out = []
    for i in text:
        out.append(table[i])
    ret = "".join(out)
    return ret

for line in sys.stdin:
    ret = transrate(line)
    print("Case #%(num)d: %(output)s" %{"num":i, "output":ret})
    i += 1
