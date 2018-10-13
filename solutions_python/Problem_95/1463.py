dict={' ':' ', 'a':'y','b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}

f = open('file.txt', 'r')
fout = open('a.out', 'w')
a = (int)(f.readline())
for i in xrange(a):
    line = f.readline()
    re = ''
    for j in xrange(len(line)-1):
        re += dict[line[j]]
    fout.write('Case #' + str(i+1) + ": " + re + "\n")
fout.close()
