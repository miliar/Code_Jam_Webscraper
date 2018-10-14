d={' ':' ',
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
   'z':'q',
   '\n':'\n'}

fin = open('1.in', 'r')
fout = open('1.out', 'w')
n = int(fin.readline())
for i in range(n):
    g = fin.readline()
    fout.write('Case #' + str(i+1) + ': ' + ''.join(map(lambda x: d[x], g)))
fin.close()
fout.close()

print('done')

    
