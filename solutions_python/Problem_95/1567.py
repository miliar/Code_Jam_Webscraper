__author__ = 'Raullen'

f = open('C-small-practice.in','r')
T = int(f.readline())
g = open('res.out','w')
res = list()

codebook = {'a':'y', 'b':'h', 'c':'e', 'd':'s',
            'e':'o', 'f':'c', 'g':'v', 'h':'x',
            'i':'d', 'j':'u', 'k':'i', 'l':'g',
            'm':'l', 'n':'b', 'o':'k', 'p':'r',
            'q':'z', 'r':'t', 's':'n', 't':'w',
            'u':'j', 'v':'p', 'w':'f', 'x':'m',
            'y':'a', 'z':'q', ' ':' ', '\n':'\n'}

for case in range(T):
    tmp = f.readline()
    out = ''
    for x in tmp:
        out = out + codebook[x]
    print 'Case #'+ str(case+1)+': '+ out

g.writelines(res)
g.close()
f.close()